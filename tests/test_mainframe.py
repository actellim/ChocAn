import unittest
from unittest.mock import MagicMock
from src.mainframe import ChocAnDB, ReportGenerator, Billing, EmployeeTerminal, MainScheduler
from src.models import ChocAnEmployee

class TestChocAnDB(unittest.TestCase):
    def setUp(self):
        # Reset singleton for testing
        ChocAnDB._instance = None
        self.db = ChocAnDB(":memory:")

    def test_crud_member(self):
        self.db.addMember(1, "Name", "Addr", "Ph", "Em")
        self.assertIsNotNone(self.db.getMember(1))
        self.db.updateMember(1, name="New Name")
        self.assertEqual(self.db.getMember(1).memberName, "New Name")
        self.db.removeMember(1)
        self.assertIsNone(self.db.getMember(1))

class TestEmployeeTerminal(unittest.TestCase):
    def setUp(self):
        ChocAnDB._instance = None
        self.term = EmployeeTerminal()
        # Hack to force terminal to use memory db if it creates its own instance
        self.term.db = ChocAnDB(":memory:")
        
        self.operator = ChocAnEmployee(1, "Op", "Operator")
        self.manager = ChocAnEmployee(2, "Mgr", "Manager")
        self.term.db.addEmployee(self.operator)
        self.term.db.addEmployee(self.manager)

    def test_manager_access(self):
        self.term.init(self.manager.ID)
        # Should succeed
        try:
            self.term.initiateManagerReport()
        except PermissionError:
            self.fail("Manager should have access")

    def test_operator_access_denied(self):
        self.term.init(self.operator.ID)
        with self.assertRaises(PermissionError):
            self.term.initiateManagerReport()

class TestBilling(unittest.TestCase):
    def test_weekly_bill_triggers_report(self):
        billing = Billing()
        with unittest.mock.patch('src.mainframe.ReportGenerator.generateWeeklyReport') as mock_report:
            billing.weeklyBill("2023-01-07")
            mock_report.assert_called_once()

if __name__ == '__main__':
    unittest.main()
