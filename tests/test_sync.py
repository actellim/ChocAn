import unittest
import os
from src.mainframe import ChocAnDB
from src.models import Service

class TestDBSync(unittest.TestCase):
    def setUp(self):
        self.db_name = "test_sync.db"
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        # Initialize DB
        db = ChocAnDB(self.db_name)
        db.conn.close()

    def tearDown(self):
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        # Reset singleton so other tests get a fresh instance
        ChocAnDB._instance = None

    def test_service_sync(self):
        # Connection A (e.g., Employee Terminal)
        ChocAnDB._instance = None
        db_a = ChocAnDB(self.db_name)
        
        # Connection B (e.g., Provider Terminal)
        # Reset singleton to force new connection
        ChocAnDB._instance = None
        db_b = ChocAnDB(self.db_name)
        
        # Initial check
        self.assertEqual(len(db_b.getAllServices()), 0)
        
        # A adds service
        s = Service(123, 100.0, "Test Service", "Desc")
        db_a.addService(s)
        
        # B should see it immediately due to the fix
        services = db_b.getAllServices()
        self.assertEqual(len(services), 1)
        self.assertEqual(services[0].Name, "Test Service")
        
        db_a.conn.close()
        db_b.conn.close()

if __name__ == '__main__':
    unittest.main()
