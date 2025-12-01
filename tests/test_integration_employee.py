import unittest
from src.mainframe import EmployeeTerminal, ChocAnDB
from src.models import ChocAnEmployee, Member

class TestIntegrationEmployee(unittest.TestCase):
    def setUp(self):
        ChocAnDB._instance = None
        self.db = ChocAnDB(":memory:")
        self.term = EmployeeTerminal()
        # Force terminal to use same DB (singleton)
        self.term.db = self.db
        self.operator = ChocAnEmployee(1, "Op", "Operator")
        self.manager = ChocAnEmployee(2, "Mgr", "Manager")
        
        self.db.addEmployee(self.operator)
        self.db.addEmployee(self.manager)

    def test_operator_crud(self):
        self.term.init(1) # Operator
        
        # Add Member
        self.term.registerMember(333, "New Member", "Addr", "Ph", "Em")
        m = self.db.getMember(333)
        self.assertIsNotNone(m)
        self.assertEqual(m.memberName, "New Member")
        
        # Update Member
        self.term.editMemberInfo(333, name="Updated Name")
        m = self.db.getMember(333)
        self.assertEqual(m.memberName, "Updated Name")

    def test_manager_report(self):
        self.term.init(2) # Manager
        
        # Should not raise error
        report = self.term.initiateManagerReport()
        self.assertIsNotNone(report)

    def test_operator_report_fail(self):
        self.term.init(1) # Operator
        with self.assertRaises(PermissionError):
            self.term.initiateManagerReport()

if __name__ == '__main__':
    unittest.main()
