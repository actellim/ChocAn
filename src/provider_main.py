import sys
from src.terminal import Terminal
from src.mainframe import ChocAnDB

def main():
    # Ensure DB is initialized
    ChocAnDB("chocan.db")
    
    terminal = Terminal()
    print("=== ChocAn Provider Terminal ===")
    
    while True:
        try:
            provider_id = input("Enter Provider ID to login (or 'q' to quit): ")
            if provider_id.lower() == 'q':
                break
            
            if not provider_id.isdigit():
                print("Invalid ID format.")
                continue
                
            terminal.init(int(provider_id))
            if not terminal.currentProvider:
                print("Provider not found.")
                continue
                
            print(f"Welcome, {terminal.currentProvider.providerName}")
            
            while True:
                print("\nOptions:")
                print("1. Validate Member (Swipe Card)")
                print("2. Record Service")
                print("3. Request Provider Directory")
                print("4. Logout")
                
                choice = input("Select option: ")
                
                if choice == '1':
                    mem_id = input("Swipe Member Card (Enter Member ID): ")
                    if mem_id.isdigit():
                        status = terminal.verifyMemberID(int(mem_id))
                        print(f"Status: {status}")
                    else:
                        print("Invalid Member ID")
                        
                elif choice == '2':
                    mem_id = input("Enter Member ID: ")
                    serv_id = input("Enter Service Code: ")
                    date = input("Enter Date (YYYY-MM-DD): ")
                    
                    if mem_id.isdigit() and serv_id.isdigit():
                        success = terminal.recordTransaction(int(serv_id), int(mem_id), date)
                        if success:
                            print("Transaction Recorded.")
                        else:
                            print("Transaction Failed (Invalid Member/Service).")
                    else:
                        print("Invalid input.")
                        
                elif choice == '3':
                    services = terminal.getProviderDirectory()
                    print("\n--- Provider Directory (DEMO ONLY) ---")
                    for s in services:
                        print(f"[{s.ID}] {s.Name} - ${s.Fee:.2f}")
                    print("--------------------------------------")
                    terminal.emailServiceList()
                    
                elif choice == '4':
                    break
                    
        except KeyboardInterrupt:
            break
            
    print("\nShutting down terminal.")

if __name__ == "__main__":
    main()
