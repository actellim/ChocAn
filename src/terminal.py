import os
import json
from datetime import datetime
from src.models import ServiceInstance, Service

class ServiceList:
    def __init__(self):
        self.list = {}

    def refresh(self, data):
        self.list = data

    def addEntry(self, service):
        self.list[service.ID] = service

    def email(self, providerID):
        print(f"Emailing service list to provider {providerID}")

class ProviderReport:
    def sum(self, date1, date2):
        # In a real app, date1 and date2 would filter the files
        # For this demo, we'll read all json files in the current dir that look like service instances
        service_instances = []
        files = [f for f in os.listdir('.') if f.startswith('service_') and f.endswith('.json')]
        
        for filename in files:
            with open(filename, 'r') as f:
                try:
                    data = json.load(f)
                    # Send to mainframe (simulated by returning list or printing)
                    # In a real distributed system, this would be a network call
                    service_instances.append(data)
                except json.JSONDecodeError:
                    pass
        
        # "Send" to mainframe
        # For the integration test, we might need to actually call the DB if we want to verify it got there
        # But the requirement says "send that to the mainframe".
        # We'll assume there's a Mainframe listener or we return it here for the caller to handle
        return service_instances

class Terminal:
    def __init__(self):
        self.currentProvider = None
        self.serviceList = ServiceList()
        self.reportRan = False

    def init(self, providerID):
        # Authenticate against Mainframe
        from src.mainframe import ChocAnDB
        db = ChocAnDB()
        provider = db.getProvider(providerID)
        if provider:
            self.currentProvider = provider
        else:
            self.currentProvider = None

    def verifyMemberID(self, memberID):
        from src.mainframe import ChocAnDB
        db = ChocAnDB()
        member = db.getMember(memberID)
        
        if not member:
            return "INVALID"
        
        # Check status (assuming status attribute exists on Member or in DB)
        # We need to update Member model or DB query to include status if not already there
        # In previous step we added status column to DB but Member model might not have it exposed
        # Let's check Member model in src/models.py first or assume we update it.
        # For now, let's assume we can get it from the DB row if we update getMember to return it
        # or we just check the status column directly here.
        
        # Actually, let's update getMember in mainframe.py to return status in the Member object
        # But Member object definition in models.py needs to support it.
        # If not, we can just query the status here for now.
        
        # Let's do a direct query for status since Member model might be fixed
        conn = db.conn
        cursor = conn.cursor()
        cursor.execute('SELECT status FROM members WHERE id = ?', (memberID,))
        row = cursor.fetchone()
        if row:
            return row['status']
        return "INVALID"

    def recordTransaction(self, serviceID, memberID, date_str):
        if not self.currentProvider:
            return False
            
        # Create ServiceInstance
        # We need to fetch Service and Member details. Mocking for now.
        from src.models import Member, Service
        from src.mainframe import ChocAnDB
        
        db = ChocAnDB()
        member = db.getMember(memberID)
        service = db.getService(serviceID)
        
        if not member or not service:
            return False
        
        # Parse date
        try:
            time = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            time = datetime.now()
            
        instance = ServiceInstance(time, self.currentProvider, member, service)
        instance.save() # Save to disk
        db.addServiceInstance(instance) # Save to DB for reports (demo shortcut)
        return True

    def getProviderDirectory(self):
        from src.mainframe import ChocAnDB
        db = ChocAnDB()
        services = db.getAllServices()
        return services

    def getMemberList(self):
        from src.mainframe import ChocAnDB
        db = ChocAnDB()
        members = db.getAllMembers()
        return members

    def updateServiceList(self):
        # Fetch from Mainframe
        pass

    def emailServiceList(self):
        if self.currentProvider:
            self.serviceList.email(self.currentProvider.providerID)

    def emailReciept(self):
        pass

    def checkProviderTimer(self):
        # Check if it's Friday 12am (simulated)
        # If so, run report
        report = ProviderReport()
        # Date range would be last week
        report.sum("start_date", "end_date")
        self.reportRan = True
