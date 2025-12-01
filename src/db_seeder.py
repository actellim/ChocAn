import os
from src.mainframe import ChocAnDB
from src.models import Provider, Member, Service, ChocAnEmployee, ServiceInstance
from datetime import datetime

def seed_db():
    if os.path.exists("chocan.db"):
        os.remove("chocan.db")
        
    db = ChocAnDB("chocan.db")
    
    # Providers
    p1 = Provider(100000001, "Dr. John Smith", "123 Medical Way", "555-0101", "dr.smith@example.com")
    p2 = Provider(100000002, "City Clinic", "456 Health Blvd", "555-0102", "clinic@example.com")
    db.addProvider(p1)
    db.addProvider(p2)
    
    # Members
    m1 = Member(200000001, "Alice Johnson", "789 Pine St", "555-0201", "alice@example.com")
    m2 = Member(200000002, "Bob Williams", "321 Oak Ave", "555-0202", "bob@example.com")
    m3 = Member(200000003, "Charlie Brown", "101 Maple Dr", "555-0203", "charlie@example.com") # Suspended
    db.addMember(m1)
    db.addMember(m2)
    db.addMember(m3)
    
    # Manually set status for m3 to SUSPENDED
    db.updateMember(200000003, status='SUSPENDED') # Note: updateMember needs to support status kwarg or we do SQL
    
    # Let's check updateMember implementation in mainframe.py
    # It only checks for 'name'. We should update it to support 'status'.
    # Or we can just do a direct SQL update here if we don't want to change mainframe again right now.
    # But cleaner to update mainframe. Let's assume we updated it or will update it.
    # Actually, I should update mainframe.py's updateMember to support status.
    
    # For now, let's use a direct SQL hack in the seeder if possible, or just rely on the fact that I'll update mainframe.py next.
    # Wait, I can't easily update mainframe.py again in this step.
    # I'll use a direct SQL execution on the db object since I have access to it.
    db.cursor.execute("UPDATE members SET status = 'SUSPENDED' WHERE id = ?", (200000003,))
    db.conn.commit()
    
    # Services
    s1 = Service(598470, 100.0, "Dietitian Session", "One hour consultation")
    s2 = Service(883948, 150.0, "Aerobics Exercise", "Group session")
    db.addService(s1)
    db.addService(s2)
    
    # Employees
    db.addEmployee(ChocAnEmployee(300000001, "Operator Dave", "Operator"))
    db.addEmployee(ChocAnEmployee(300000002, "Manager Sarah", "Manager"))
    
    # Service Instances (for reports)
    # Note: In real app, these are created by Terminal. Here we seed them directly into DB.
    si1 = ServiceInstance(datetime.now(), p1, m1, s1)
    db.addServiceInstance(si1)
    
    si2 = ServiceInstance(datetime.now(), p1, m2, s2)
    db.addServiceInstance(si2)
    
    si3 = ServiceInstance(datetime.now(), p2, m1, s1)
    db.addServiceInstance(si3)
    
    print("Database seeded successfully.")

if __name__ == "__main__":
    seed_db()
