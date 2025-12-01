import sys
from src.mainframe import EmployeeTerminal, ChocAnDB
from src.models import Member, Provider

def main():
    ChocAnDB("chocan.db")
    terminal = EmployeeTerminal()
    
    print("=== ChocAn Employee Terminal ===")
    
    while True:
        try:
            emp_id_input = input("Enter Employee ID to Login (or 'q' to quit): ")
            if emp_id_input.lower() == 'q':
                break
                
            if not emp_id_input.isdigit():
                print("Invalid ID format.")
                continue
                
            emp_id = int(emp_id_input)
            terminal.init(emp_id)
            
            if not terminal.currentEmployee:
                print("Login Failed: Employee not found.")
                continue
                
            print(f"Welcome, {terminal.currentEmployee.name} ({terminal.currentEmployee.role})")
            
            if terminal.currentEmployee.role == "Operator":
                # ... (Operator menu remains same)
                while True:
                    print("\n--- Operator Menu ---")
                    print("1. Manage Members (Add/Update/Remove)")
                    print("2. Manage Providers (Add/Update/Remove)")
                    print("3. Manage Services (Add)")
                    print("4. Logout")
                    
                    choice = input("Select option: ")
                    
                    if choice == '1':
                        print("  a. Add Member")
                        print("  b. Update Member")
                        print("  c. Remove Member")
                        sub = input("  Select: ")
                        try:
                            if sub == 'a':
                                mid = int(input("ID: "))
                                name = input("Name: ")
                                addr = input("Address: ")
                                phone = input("Phone: ")
                                email = input("Email: ")
                                terminal.registerMember(mid, name, addr, phone, email)
                                print("Member added.")
                            elif sub == 'b':
                                mid = int(input("Member ID: "))
                                name = input("New Name: ")
                                terminal.editMemberInfo(mid, name=name)
                                print("Member updated.")
                            elif sub == 'c':
                                mid = int(input("Member ID: "))
                                success = terminal.removeMember(mid)
                                if success:
                                    print("Member removed.")
                                else:
                                    print("Member not found.")
                        except Exception as e:
                            print(f"Error: {e}")

                    elif choice == '2':
                        print("  a. Add Provider")
                        print("  b. Update Provider")
                        print("  c. Remove Provider")
                        sub = input("  Select: ")
                        try:
                            if sub == 'a':
                                pid = int(input("ID: "))
                                name = input("Name: ")
                                addr = input("Address: ")
                                phone = input("Phone: ")
                                email = input("Email: ")
                                terminal.registerProvider(Provider(pid, name, addr, phone, email))
                                print("Provider added.")
                            elif sub == 'b':
                                pid = int(input("Provider ID: "))
                                name = input("New Name: ")
                                terminal.updateProvider(pid, name=name)
                                print("Provider updated.")
                            elif sub == 'c':
                                pid = int(input("Provider ID: "))
                                success = terminal.removeProvider(pid)
                                if success:
                                    print("Provider removed.")
                                else:
                                    print("Provider not found.")
                        except Exception as e:
                            print(f"Error: {e}")

                    elif choice == '3':
                        try:
                            sid = int(input("Service ID: "))
                            fee = float(input("Fee: "))
                            name = input("Name: ")
                            desc = input("Desc: ")
                            terminal.registerService(Service(sid, fee, name, desc))
                            print("Service added.")
                        except Exception as e:
                            print(f"Error: {e}")

                    elif choice == '4':
                        break

            elif terminal.currentEmployee.role == "Manager":
                while True:
                    print("\n--- Manager Menu ---")
                    print("1. Run Reports")
                    print("2. Manage Employees (Add/Update/Remove)")
                    print("3. Logout")
                    
                    choice = input("Select option: ")
                    
                    if choice == '1':
                        try:
                            pid_input = input("Enter Provider ID (optional, press Enter for all): ")
                            pid = int(pid_input) if pid_input else None
                            report = terminal.initiateManagerReport(pid)
                            print(f"\n{report}")
                        except Exception as e:
                            print(f"Error: {e}")

                    elif choice == '2':
                        print("  a. Add Employee")
                        print("  b. Update Employee")
                        print("  c. Remove Employee")
                        sub = input("  Select: ")
                        try:
                            if sub == 'a':
                                eid = int(input("ID: "))
                                name = input("Name: ")
                                role = input("Role (Operator/Manager): ")
                                terminal.registerEmployee(ChocAnEmployee(eid, name, role))
                                print("Employee added.")
                            elif sub == 'b':
                                eid = int(input("Employee ID: "))
                                name = input("New Name (leave blank to keep): ")
                                role = input("New Role (Operator/Manager, leave blank to keep): ")
                                kwargs = {}
                                if name: kwargs['name'] = name
                                if role: kwargs['role'] = role
                                
                                if kwargs:
                                    terminal.editEmployee(eid, **kwargs)
                                    print("Employee updated.")
                                else:
                                    print("No changes made.")
                            elif sub == 'c':
                                eid = int(input("Employee ID: "))
                                if eid == terminal.currentEmployee.ID:
                                    print("Error: Cannot remove yourself.")
                                else:
                                    success = terminal.removeEmployee(eid)
                                    if success:
                                        print("Employee removed.")
                                    else:
                                        print("Employee not found.")
                        except Exception as e:
                            print(f"Error: {e}")

                    elif choice == '3':
                        break
                    
        except KeyboardInterrupt:
            break
            
    print("\nShutting down.")

if __name__ == "__main__":
    main()
