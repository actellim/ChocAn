import unittest
import os
from src.terminal import Terminal
from src.mainframe import ChocAnDB
from src.models import Provider, Member, Service

class TestIntegrationProvider(unittest.TestCase):
    def setUp(self):
        # Setup shared DB
        ChocAnDB._instance = None
        self.db = ChocAnDB(":memory:")
        self.terminal = Terminal()
        # Ensure terminal uses same DB instance (singleton handles this if initialized correctly)
        # But Terminal.init lazy loads Provider which calls DB. 
        # We need to make sure Terminal uses our memory DB.
        # Since ChocAnDB is a singleton, as long as we init it first with :memory:, subsequent calls get the same instance.
        
        # Seed DB
        self.provider = Provider(111111111, "Dr. Smith", "123 St", "555-1111", "dr@smith.com")
        self.member = Member(222222222, "John Doe", "456 Ave", "555-2222", "john@doe.com")
        self.service = Service(101, 50.0, "Checkup", "General Checkup")
        
        self.db.addProvider(self.provider)
        self.db.addMember(self.member)
        self.db.addService(self.service)

    def test_provider_service_flow(self):
        # 1. Provider logs in
        self.terminal.init(111111111)
        self.assertEqual(self.terminal.currentProvider.providerID, 111111111)
        
        # 2. Verify Member
        status = self.terminal.verifyMemberID(222222222)
        self.assertEqual(status, "VALIDATED")
        
        # 3. Record Transaction
        # This should save a file to disk
        self.terminal.recordTransaction(101, 222222222, "2023-11-30")
        
        # Verify file exists (implementation detail: how filename is generated)
        # For this test, we might need to check if ANY json file was created or mock the filename generation
        # Assuming we can check the DB or a known file location if the system was fully integrated
        # But per requirements, it saves to disk first.
        # Let's check if the terminal has a way to expose the last saved file or we check the directory
        files = [f for f in os.listdir('.') if f.endswith('.json')]
        self.assertTrue(len(files) > 0)
        
        # Cleanup
        for f in files:
            os.remove(f)

if __name__ == '__main__':
    unittest.main()
