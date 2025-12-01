import unittest
import os
import json
from datetime import datetime
# We will create these classes later
from src.models import Provider, Member, Service, ServiceInstance, ChocAnEmployee

class TestModels(unittest.TestCase):
    def test_provider_validation(self):
        p = Provider(123456789, "Test Provider", "123 Main St", "555-0100", "test@example.com")
        self.assertTrue(p.checkProviderID(123456789))
        self.assertFalse(p.checkProviderID(999999999))
        self.assertEqual(p.getProviderID(), 123456789)

    def test_member_validation(self):
        m = Member(987654321, "Test Member", "456 Oak St", "555-0200", "member@example.com")
        self.assertTrue(m.checkMemberID(987654321))
        self.assertFalse(m.checkMemberID(111111111))

    def test_service_attributes(self):
        s = Service(101, 50.0, "Therapy", "Standard Session")
        self.assertEqual(s.ID, 101)
        self.assertEqual(s.Fee, 50.0)
        self.assertEqual(s.Name, "Therapy")

    def test_service_instance_save(self):
        # Setup
        filename = "service_instance_test.json"
        if os.path.exists(filename):
            os.remove(filename)
            
        si = ServiceInstance(
            datetime.now(),
            Provider(1, "P", "A", "P", "E"),
            Member(2, "M", "A", "P", "E"),
            Service(3, 10.0, "S", "D")
        )
        si.save(filename)
        
        # Verify
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as f:
            data = json.load(f)
            self.assertEqual(data['service_code'], 3)
            self.assertEqual(data['provider_id'], 1)
            self.assertEqual(data['member_id'], 2)
            
        # Cleanup
        if os.path.exists(filename):
            os.remove(filename)

    def test_employee_roles(self):
        op = ChocAnEmployee(1, "Operator", "Operator")
        mgr = ChocAnEmployee(2, "Manager", "Manager")
        self.assertEqual(op.role, "Operator")
        self.assertEqual(mgr.role, "Manager")

if __name__ == '__main__':
    unittest.main()
