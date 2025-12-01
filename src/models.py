import json
from datetime import datetime

class Provider:
    def __init__(self, providerID, providerName, providerAddress, providerPhone, providerEMail):
        self.providerID = providerID
        self.providerName = providerName
        self.providerAddress = providerAddress
        self.providerPhone = providerPhone
        self.providerEMail = providerEMail

    def checkProviderID(self, providerID):
        # In a real system, this might check against a DB or checksum
        # For this demo, we'll just check if it matches the ID initialized
        return self.providerID == providerID

    def getProviderID(self):
        return self.providerID

class Member:
    def __init__(self, memberID, memberName, memberAddress, memberPhone, memberEMail):
        self.memberID = memberID
        self.memberName = memberName
        self.memberAddress = memberAddress
        self.memberPhone = memberPhone
        self.memberEMail = memberEMail

    def checkMemberID(self, memberID):
        return self.memberID == memberID

class Service:
    def __init__(self, ID, Fee, Name, Desc):
        self.ID = ID
        self.Fee = Fee
        self.Name = Name
        self.Desc = Desc

class ServiceInstance:
    def __init__(self, time, provider, member, service):
        self.time = time
        self.provider = provider
        self.member = member
        self.service = service

    def save(self, filename=None):
        if filename is None:
            # Generate a filename based on time if not provided
            filename = f"service_{self.time.strftime('%Y%m%d%H%M%S')}.json"
            
        data = {
            "current_date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "service_date": self.time.strftime("%Y-%m-%d"),
            "provider_number": self.provider.providerID,
            "member_number": self.member.memberID,
            "service_code": self.service.ID,
            "comments": "", # Optional
            # For test verification
            "provider_id": self.provider.providerID,
            "member_id": self.member.memberID
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f)

class ChocAnEmployee:
    def __init__(self, ID, name, role):
        self.ID = ID
        self.name = name
        self.role = role # 'Operator' or 'Manager'
