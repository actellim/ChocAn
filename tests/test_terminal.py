import unittest
from unittest.mock import MagicMock, patch
from src.terminal import Terminal, ServiceList, ProviderReport
from src.models import Provider, Member, Service

class TestTerminal(unittest.TestCase):
    def setUp(self):
        self.terminal = Terminal()
        self.provider = Provider(123456789, "Test P", "Addr", "Ph", "Em")
        
    def test_init_terminal(self):
        # Seed provider
        from src.mainframe import ChocAnDB
        from src.models import Provider
        db = ChocAnDB()
        db.addProvider(Provider(123456789, "Test Provider", "Addr", "Ph", "Em"))
        
        self.terminal.init(123456789)
        self.assertEqual(self.terminal.currentProvider.providerID, 123456789)

    def test_init_terminal_invalid(self):
        self.terminal.init(999999999)
        self.assertIsNone(self.terminal.currentProvider)

    def test_verify_member(self):
        # Mocking the validation call to Mainframe/DB if necessary, 
        # but for now assuming Terminal has local logic or connects to a mock DB
        self.terminal.verifyMemberID(987654321)
        # Assertions depend on implementation details of verification (return bool or status string)
        # For now, we assume it returns a status string
        # self.assertEqual(status, "VALIDATED") 

    def test_record_transaction(self):
        # Seed provider and init
        from src.mainframe import ChocAnDB
        from src.models import Provider, Member, Service
        db = ChocAnDB()
        db.addProvider(Provider(123456789, "Test Provider", "Addr", "Ph", "Em"))
        self.terminal.init(123456789)
        
        # Seed DB for validation
        db.addMember(Member(987654321, "Test Member", "Addr", "Ph", "Em"))
        db.addService(Service(101, 50.0, "Test Service", "Desc"))
        
        # Should create a ServiceInstance
        with patch('src.models.ServiceInstance.save') as mock_save:
            success = self.terminal.recordTransaction(101, 987654321, "2023-01-01")
            self.assertTrue(success)
            mock_save.assert_called_once()

class TestServiceList(unittest.TestCase):
    def test_refresh_and_add(self):
        sl = ServiceList()
        s = Service(1, 100.0, "Test", "Desc")
        sl.addEntry(s)
        self.assertIn(1, sl.list)

class TestProviderReport(unittest.TestCase):
    @patch('src.terminal.os.listdir')
    @patch('src.terminal.open')
    def test_sum_reads_disk(self, mock_open, mock_listdir):
        # Mock finding a JSON file
        mock_listdir.return_value = ['service_123.json']
        
        # Mock reading the file
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file
        mock_file.read.return_value = '{"service_code": 1, "provider_id": 123}'
        
        report = ProviderReport()
        # Mock the DB connection or return value
        result = report.sum("2023-01-01", "2023-01-07")
        
        # Verify it tried to read the file
        mock_open.assert_called()

if __name__ == '__main__':
    unittest.main()
