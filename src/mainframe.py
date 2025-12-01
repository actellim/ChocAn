import sqlite3
from datetime import datetime
from src.models import Provider, Member, Service, ChocAnEmployee

class ChocAnDB:
    _instance = None
    DB_FILE = "chocan.db"
    
    def __new__(cls, db_file=None):
        if cls._instance is None:
            cls._instance = super(ChocAnDB, cls).__new__(cls)
            if db_file:
                cls._instance.DB_FILE = db_file
            cls._instance._init_db()
        return cls._instance

    def _init_db(self):
        self.conn = sqlite3.connect(self.DB_FILE)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        
        # Create tables
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS providers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                phone TEXT,
                email TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                phone TEXT,
                email TEXT,
                status TEXT DEFAULT 'VALIDATED'
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY,
                fee REAL,
                name TEXT,
                desc TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                role TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS service_instances (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                provider_id INTEGER,
                member_id INTEGER,
                service_code INTEGER,
                comments TEXT,
                uploaded_time TEXT
            )
        ''')
        self.conn.commit()

    def addProvider(self, provider):
        self.cursor.execute('''
            INSERT OR REPLACE INTO providers (id, name, address, phone, email)
            VALUES (?, ?, ?, ?, ?)
        ''', (provider.providerID, provider.providerName, provider.providerAddress, provider.providerPhone, provider.providerEMail))
        self.conn.commit()

    def removeProvider(self, providerID):
        self.cursor.execute('DELETE FROM providers WHERE id = ?', (providerID,))
        self.conn.commit()

    def updateProvider(self, providerID, **kwargs):
        # Construct query dynamically
        if not kwargs: return
        
        fields = []
        values = []
        for k, v in kwargs.items():
            if k == 'name': fields.append("name = ?")
            # Add other mappings as needed
            values.append(v)
        
        values.append(providerID)
        query = f"UPDATE providers SET {', '.join(fields)} WHERE id = ?"
        self.cursor.execute(query, tuple(values))
        self.conn.commit()

    def getProvider(self, providerID):
        self.cursor.execute('SELECT * FROM providers WHERE id = ?', (providerID,))
        row = self.cursor.fetchone()
        if row:
            return Provider(row['id'], row['name'], row['address'], row['phone'], row['email'])
        return None

    def addMember(self, *args):
        if len(args) == 1 and isinstance(args[0], Member):
            member = args[0]
            self.cursor.execute('''
                INSERT OR REPLACE INTO members (id, name, address, phone, email)
                VALUES (?, ?, ?, ?, ?)
            ''', (member.memberID, member.memberName, member.memberAddress, member.memberPhone, member.memberEMail))
        elif len(args) == 5:
             self.cursor.execute('''
                INSERT OR REPLACE INTO members (id, name, address, phone, email)
                VALUES (?, ?, ?, ?, ?)
            ''', args)
        self.conn.commit()

    def removeMember(self, memberID):
        self.cursor.execute('DELETE FROM members WHERE id = ?', (memberID,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def updateMember(self, memberID, **kwargs):
        if not kwargs: return
        fields = []
        values = []
        for k, v in kwargs.items():
            if k == 'name': fields.append("name = ?")
            if k == 'address': fields.append("address = ?")
            if k == 'phone': fields.append("phone = ?")
            if k == 'email': fields.append("email = ?")
            if k == 'status': fields.append("status = ?")
            values.append(v)
            
        if not fields: return # Nothing to update
        
        values.append(memberID)
        query = f"UPDATE members SET {', '.join(fields)} WHERE id = ?"
        self.cursor.execute(query, tuple(values))
        self.conn.commit()

    def getMember(self, memberID):
        self.cursor.execute('SELECT * FROM members WHERE id = ?', (memberID,))
        row = self.cursor.fetchone()
        if row:
            return Member(row['id'], row['name'], row['address'], row['phone'], row['email'])
        return None

    def addService(self, service):
        self.cursor.execute('''
            INSERT OR REPLACE INTO services (id, fee, name, desc)
            VALUES (?, ?, ?, ?)
        ''', (service.ID, service.Fee, service.Name, service.Desc))
        self.conn.commit()

    def getService(self, serviceID):
        self.cursor.execute('SELECT * FROM services WHERE id = ?', (serviceID,))
        row = self.cursor.fetchone()
        if row:
            return Service(row['id'], row['fee'], row['name'], row['desc'])
        return None

    def addEmployee(self, employee):
        self.cursor.execute('''
            INSERT OR REPLACE INTO employees (id, name, role)
            VALUES (?, ?, ?)
        ''', (employee.ID, employee.name, employee.role))
        self.conn.commit()

    def updateEmployee(self, employeeID, **kwargs):
        if not kwargs: return
        fields = []
        values = []
        for k, v in kwargs.items():
            if k == 'name': fields.append("name = ?")
            if k == 'role': fields.append("role = ?")
            values.append(v)
        values.append(employeeID)
        query = f"UPDATE employees SET {', '.join(fields)} WHERE id = ?"
        self.cursor.execute(query, tuple(values))
        self.conn.commit()

    def removeEmployee(self, employeeID):
        self.cursor.execute('DELETE FROM employees WHERE id = ?', (employeeID,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def getEmployee(self, employeeID):
        self.cursor.execute('SELECT * FROM employees WHERE id = ?', (employeeID,))
        row = self.cursor.fetchone()
        if row:
            return ChocAnEmployee(row['id'], row['name'], row['role'])
        return None

    def getAllMembers(self):
        self.conn.commit() # Force refresh to see changes from other connections
        self.cursor.execute('SELECT * FROM members')
        rows = self.cursor.fetchall()
        return [Member(r['id'], r['name'], r['address'], r['phone'], r['email']) for r in rows]

    def getAllServices(self):
        self.conn.commit() # Force refresh to see changes from other connections
        self.cursor.execute('SELECT * FROM services')
        rows = self.cursor.fetchall()
        return [Service(r['id'], r['fee'], r['name'], r['desc']) for r in rows]

    def addServiceInstance(self, instance):
        # For demo, we might want to save instances to DB for reports
        self.cursor.execute('''
            INSERT INTO service_instances (date, provider_id, member_id, service_code, comments, uploaded_time)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (instance.time.strftime("%Y-%m-%d"), instance.provider.providerID, instance.member.memberID, instance.service.ID, "", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.conn.commit()

    def getServiceInstances(self, providerID=None, dateRange=None):
        # Simple query for demo
        query = "SELECT * FROM service_instances"
        params = []
        if providerID:
            query += " WHERE provider_id = ?"
            params.append(providerID)
        
        self.cursor.execute(query, tuple(params))
        return self.cursor.fetchall()

class ReportGenerator:
    def generateReport(self, employee, dateRange, providerID=None):
        db = ChocAnDB()
        instances = db.getServiceInstances(providerID, dateRange)
        
        report = f"Report generated by {employee.name}\n"
        report += f"Date Range: {dateRange}\n"
        if providerID:
            report += f"Provider ID: {providerID}\n"
        report += "-" * 30 + "\n"
        
        total_fee = 0.0
        consultations = 0
        
        for inst in instances:
            # Fetch details
            service = db.getService(inst['service_code'])
            member = db.getMember(inst['member_id'])
            provider = db.getProvider(inst['provider_id'])
            
            fee = service.Fee if service else 0.0
            total_fee += fee
            consultations += 1
            
            report += f"Date: {inst['date']}\n"
            report += f"Provider: {provider.providerName if provider else 'Unknown'} ({inst['provider_id']})\n"
            report += f"Member: {member.memberName if member else 'Unknown'}\n"
            report += f"Service: {service.Name if service else 'Unknown'} (Fee: ${fee:.2f})\n"
            report += "-" * 10 + "\n"
            
        report += f"Total Consultations: {consultations}\n"
        report += f"Total Fee: ${total_fee:.2f}\n"
        return report

    def generateWeeklyReport(self):
        print("Generating weekly report...")
        return "Weekly Report Generated"

class Billing:
    def __init__(self):
        self.payouts = {}

    def weeklyBill(self, date):
        # Calculate payouts
        # Trigger report generation
        gen = ReportGenerator()
        gen.generateWeeklyReport()

class MainScheduler:
    def checkAcmeTimer(self):
        # Check if it's Saturday 12am
        # Trigger Billing
        billing = Billing()
        billing.weeklyBill("today")

class EmployeeTerminal:
    def __init__(self):
        self.db = ChocAnDB()
        self.currentEmployee = None

    def init(self, employeeID):
        self.currentEmployee = self.db.getEmployee(employeeID)

    def _check_operator(self):
        if not self.currentEmployee: raise PermissionError("Not logged in")
        if self.currentEmployee.role != "Operator": raise PermissionError("Access Denied: Operators only")

    def _check_manager(self):
        if not self.currentEmployee: raise PermissionError("Not logged in")
        if self.currentEmployee.role != "Manager": raise PermissionError("Access Denied: Managers only")

    def registerMember(self, *args, **kwargs):
        self._check_operator()
        self.db.addMember(*args, **kwargs)

    def editMemberInfo(self, memberID, **kwargs):
        self._check_operator()
        self.db.updateMember(memberID, **kwargs)

    def removeMember(self, memberID):
        self._check_operator()
        return self.db.removeMember(memberID)

    def suspendMember(self, memberID):
        self._check_operator()
        self.db.updateMember(memberID, status='SUSPENDED')

    def registerProvider(self, provider):
        self._check_operator()
        self.db.addProvider(provider)

    def updateProvider(self, providerID, **kwargs):
        self._check_operator()
        self.db.updateProvider(providerID, **kwargs)

    def removeProvider(self, providerID):
        self._check_operator()
        return self.db.removeProvider(providerID)

    def registerService(self, service):
        self._check_operator()
        self.db.addService(service)

    # Employee CRUD for Managers
    def registerEmployee(self, employee):
        self._check_manager()
        self.db.addEmployee(employee)

    def editEmployee(self, employeeID, **kwargs):
        self._check_manager()
        # We need to implement updateEmployee in ChocAnDB first
        # For now, let's assume we add it or do it here
        # Better to add to DB class.
        self.db.updateEmployee(employeeID, **kwargs)

    def removeEmployee(self, employeeID):
        self._check_manager()
        if self.currentEmployee.ID == employeeID:
            raise ValueError("Cannot remove yourself")
        # Implement removeEmployee in DB
        return self.db.removeEmployee(employeeID)

    def initiateManagerReport(self, providerID=None):
        self._check_manager()
        gen = ReportGenerator()
        return gen.generateReport(self.currentEmployee, "Last Week", providerID)
