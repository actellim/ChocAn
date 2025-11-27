# Noun Extraction

## Use Case List

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

## Candidate Classes

- Member
- Provider
- Provider Services/Services
- Service Fees
- Billing
- ChocAn Database
- ChocAn Employees

