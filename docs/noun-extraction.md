# Noun Extraction

## Use Case List

| Use Case | Brief Description |
|----------|------------------|
| Verify Member Number | Allows a provider to check if a member number is valid or suspended |
| Verify Provider Number | Allows a provider to confirm that their provider number is registered in the ChocAn system |
| Request Provider Directory | Allows the provider to view the list of services service codes and fees |
| Lookup Service Code | Retrieves the service name for a given service code |
| Lookup Fee | Retrieves the fee for a given service code |
| Record Service Provided | Allows a provider to enter a completed service including date service code and comments then store it in the Data Center |
| Retrieve Services | Gets all services a provider completed within the week |
| Weekly Report Generation | Produces weekly reports for members providers and the manager |
| Weekly Accounting | Sends weekly fee totals and provider payments amounts to Acme Accounting Services |
| Print Financial Report | Prints the weekly financial summary |
| Add Provider | Allows the ChocAn operator to add a provider |
| Delete Provider | Allows the ChocAn operator to remove a provider |
| Update Provider | Allows the ChocAn operator to update provider information |
| Add Member | Allows the ChocAn operator to add a member |
| Delete Member | Allows the ChocAn operator to remove a member |
| Update Member | Allows the ChocAn operator to update member information |
| Add Service Code | Allows the ChocAn operator to add a new service code |
| Update Service Code | Allows the ChocAn operator to update a service code |
| Delete Service Code | Allows the ChocAn operator to delete a service code |
| Get Weekly Fees | Retrieves total fees for the current or previous week |

## Use Case Noun List

*Contains nouns extracted from use cases.*

| Use Case | Nouns |
|---|---|
| Verify Member Number (Provider) | Providers, Person, ChocAn, membership. |
| Verify Provider Number (Provider) | Providers, ChocAn system, accounting. |
| Request Provider Directory | Providers, services, service number, fees. |
| Lookup Service Code | Terminal, ChocAn data center, list, service codes, descriptions. |
| Lookup Fee | Service Code, service fee. |
| Bill ChocAn | Provider's Terminals, bill, ChocAn database, services, codes, fees, provider number. |
| Calculate Weekly Fee | List, Service Codes, Terminal, Week, Fees. |
| Check Member Number (Server) | Member Number, Database. |
| Check Provider Number (Server) | Provider Number, ChocAn Database. |
| Check Service Code | Server, Service Code, Descriptions, Terminal. |
| Check Fee | List, Service Code, Fees. |
| Store Weekly Fees | List, Services, Fees, Fee Total, Provider, Week. |
| Weekly Report Generation | Provider, Fees, Week, Database. |
| Weekly Accounting | Fees, Report Generation, Acme Accounting Services. |
| Print Financial Report | Fees, Database, Week. |
| Add Provider | ChocAn Operator, provider, ChocAn database. |
| Delete Provider | ChocAn Operator, Provider, ChocAn database. |
| Update Provider | ChocAn Operator, Provider, Details, ChocAn database. |
| Add Member | ChocAn Operator, Member, ChocAn database. |
| Delete Member | ChocAn Operator, Member, ChocAn database. |
| Update Member | ChocAn Operator, Details, Member, ChocAn database. |
| Add Service Code | ChocAn Operator, Service Code, Service Directory. |
| Update Service Code | ChocAn Operator, Service Code, Service Directory. |
| Delete Service Code | ChocAn Operator, Service Code, Service Directory. |
| Get Weekly Fees | Fees, Database, Week. |
| Retrieve Services | Services, Provider, Week. |
| Save Service | Provider, Services, Terminal, ChocAn Data Center. |
:Table containing nouns extracted from use cases.

## Noun List

*A list of nouns extracted from the use cases*.

- [x] Providers
- [x] Person
- [x] ChocAn
- [x] Membership
- [x] ChocAn System
- [x] Accounting
- [x] Services
- [x] Service Number
- [x] Fees
- [x] Terminal
- [X] ChocAn Data Cenber
- [ ] List
- [x] Service Codes
- [ ] Descriptions
- [x] Service Fee
- [x] Provider's Terminals
- [x] Bill
- [x] ChocAn Database
- [x] Codes
- [x] Provider Number
- [ ] Week
- [x] Member Number
- [x] Database
- [x] Server
- [ ] Descriptions
- [x] Fee Total
- [x] Report Generation
- [x] Acme Accounting Services
- [x] ChocAn Operator
- [ ] Details
- [x] Member
- [x] Service Directory

## Noun Grouping

*A section grouping the nouns extracted from the use cases.*

### Member

- Person/Member
- Member Number
- Membership

### Provider 

- Provider
- Provider Number
- Terminal/Provider's Terminal

### Provider Services

- Services
- Codes/Service Codes
- Service Directory
- Service Number
- Service Fees

### Service Fees

- Fees/Service Fees
- Fee Total

### Billing

- Accounting
- Report Generation
- Bill
- Acme Accounting Services

### ChocAn Database

- ChocAn/Server/Database/ChocAn Database/ChocAn System/ChocAn Data Center

### ChocAn Employees

- ChocAn Manager
- ChocAn Operator

## Candidate Class List

- Member
- Provider
- Services/Provider Services
- Service Fees
- Billing
- ChocAn Database
- ChocAn Employees

## Candidate Class Expansion

---

### Provider Terminal

#### Terminal

- Attributes:
    - Provider
    - reportRan: bool
- Methods:
    - Provider init(providerID)
    - verifyProviderID(providerID)
    - verifyMemberID(memberID)
    - recordTransaction(serviceID, memberID, time)
    - updateServiceList()
    - emailServiceList()
    - emailReciept()
    - checkProviderTimer()

#### Member

- Attributes:
    public:
    - memberID: int
    private
    - memberName: string
    - memberAddress: string
    - memberPhone: string
    - memberEMail: string

#### Provider

- Attributes:
    public
    - providerID: int
    private
    - providerName: string
    - providerAddress: string
    - providerPhone: string
    - providerEMail: string

#### ServiceInstance

- Attributes:
    - rendered: Service
    - customer: Member
    - provider: Provider
    - time: arr(Date, Time)
- Methods:
    - save()            // Saves an instance of a service locally

#### ServiceList

- Attributes:
    - List: dict{id: Service}
- Methods:
    - refresh()         // Re-pulls from the database.
    - email(providerID) // E-mails the current service list to the provider.

#### Service

- Attributes:
    - ID: int
    - Fee: float(2)
    - Name: string
    - Desc: string

#### ProviderReport

- Attributes:
    - weeklyServices: arr[serviceInstance]
- Methods:
    - sum(date1, date2) // Gets all service instances in a range and totals
                        // the fee.

---

### ChocAn Mainframe

#### EmployeeTerminal

- Attributes:
    - employee: ChocAnEmployee
    - dbInstance: ChocAnDB
- Methods:
    - ChocAnEmployee, ChocAnDB init(EmployeeID)
    - registerMember()
    - editMemberInfo()
    - viewMemberInfo()
    - suspendMember()
    - hireEmployee()
    - updateEmployeeInfo()
    - viewEmployeeInfo()
    - fireEmployee()
    - registerProvider()
    - editProviderInfo()
    - viewProviderInfo()
    - suspendProvider()
    - registerService()
    - editServiceInfo()
    - viewServiceInfo()
    - suspendService()
    - initiateManagerReport()

#### MainScheduler

- Attributes:
    - timerRan: bool
- Methods
    - checkAcmeTimer()

#### ReportGenerator

- Attributes:
    - services: arr[ServiceInstance]
    - date: date
- Methods
    - generateReport(ChocAnEmployee, date1, date2, providerID(optional))        // Called by ChocAn managers over a date range. Can specify a provider.
    - generateWeeklyReport()                                                    // Automatically called weekly for the billing class.

#### Billing

- Attributes:
    - payouts: dict{providerID: FeeTotal}
    - period: date
- Methods:
    - weeklyBill(date)       // Gets the total fee for each provider for the previous week from the ReportGenerator and sends it to ACMEAccounting.

#### ChocAnDB

- Methods:
    - addEmployee()
    - removeEmployee(employeeID)
    - updateEmployee(employeeID)
    - viewEmployee(employeeID)
    - addMember()
    - removeMember(memberID)
    - updateMember(memberID)
    - viewMember(memberID)
    - addProvider()
    - removeProvider(providerID)
    - updateProvider(providerID)
    - viewProvider(providerID)
    - addService()
    - removeService(serviceID)
    - updateService(serviceID)
    - viewService(serviceID)
    - getServiceList()
    - getWeeklyServices(date)
    - getServices(date1, date2)

#### ChocAnEmployee

- Attributes:
    - ID: int
    - name: string
    - role: string

