---
title: Software Project Management Plan
subtitle: For the ChocAn Project
---

# Software Project Management Plan

## Overview

### Project Summary

#### Purpose Scope and Objectives

The goal is to build ChocAn’s Project, a software product that supports provider terminal and ChocAn database interaction.  
The product will let the client add, edit, and delete the needed records, run the required checks, and produce weekly reports and payment files.  
**Objectives:**

* Deliver a working product that meets all stated requirements and ship the product to the client on time.  
* Produce clear reports and correct totals.

#### Assumptions and Constraints

* We must meet the deadline and stay within the budget.  
* The product must be reliable and easy to maintain.  
* The design must allow new features later.  
* The user interface must be simple.

#### Project Deliverables

* Working product.  
* User guide.  
* Technical notes and setup guide.  
* Test results and acceptance record.

#### Schedule and Budget Summary

Workflows with time, people, and internal cost.

* Requirements workflow – 3 week two people $0.  
* Analysis workflow – 1 week two people $0.  
* Design workflow – 1 week two people $0.  
* Implementation workflow – 1 week three people $0.  
* Testing workflow – 1 week three people $0.  
* Total 10 weeks and $0.

#### Evolution of the Plan

Any change to this plan must be approved by the engineering team, and recorded so the plan stays current.

## Reference Materials

All work will follow the textbook standards for coding documents, testing, and reviews. 

## Definitions and Acronyms

List the terms used in this plan

* **ChocAn**: The client company.  
* **Client**: the sponsor or user of the system.  
* **DataCenter**: the main system that stores records and runs reports.  
* **EFT**: electronic funds transfer file for provider payments.  
* **UI**: user interface.  
* **DB**: database.

## Project Organization

### External Interfaces

* **Client contact**: ChocAn Head Office/Dr. A. Diyab with questions.

### Internal Structure

**Team of three:**

* **Kenneth:** software engineering student  
* **Vu:** software engineering student  
* **Josh:** software engineering student

### Roles and Responsibilities

* Engineering communicates via e-mail if they have questions, keep records current on the git project, and escalate questions to Dr. Diyab via e-mail.  
* Engineering Student A owns features \[area A for example reports and operating data\].  
* Engineering Student B owns features \[area B for example services and payments\].  
* Engineering Student C owns features \[area C for example version tracking and mergers\].  
* Each member is responsible for the quality of their artifacts.

## Managerial Process Plans

### Start up Plan

#### Estimation Plan

Total time 7 weeks total internal cost $0 based on past class project deadline.

#### Staffing Plan

* Three engineering students are needed for all 10 weeks first 5 weeks as analysts and designers then as developers and testers.

#### Resource Acquisition Plan

All tools and machines are available. The product will be delivered as source code, and the client will be expected to compile it in their environment.

#### Project Staff Training Plan

The engineers will be responsible for **first** reviewing the textbook and **then** consulting AI with any follow-up questions about their roles.

### Work Plan

#### Work Activities 

* Week 1-3 gather and inspect requirements, meet with the client, define group setup, and confirm scope.  
* Weeks 4 build analysis artifacts and inspect them, then get client approval.  
* Weeks 5 build design artifacts and inspect them.  
* Weeks 6-7 begin implementation by writing tests, then implement classes, integrate them, write docs, and do the final inspection.

#### Schedule Allocation

#### Resource Allocation

Each member works on assigned artifacts. Bi-weekly stand up to track progress and blockers. Bi-weekly client meeting (class) to confirm any scope changes.

#### Budget Allocation

|Activity|Cost|
|---|---|
|Requirements| \$0|
|Analysis| \$0|
|Design| \$0  |
|Implementation| \$0  |
| Testing| \$0|
| Total | \$0|

### Control Plan

Any change that affects time or budget must be approved by the engineering team and recorded. Each person tests another person's work to keep quality.

### Risk Management Plan

Main risks and how we track them

* No existing product to compare so we plan strong testing.  
* The client has limited technical background so we keep screens simple and review often.  
* Find any possible design fault so we inspect the design and write tests early.  
* Possible machine or tool failure so we keep a spare machine or switch tools if needed.  
* Performance risk is low due to small size but we will monitor response time.

### Project Close out Plan

Give the client the product, user guide, test results, and acceptance note. Collect lessons learned.

## Technical Process Plans

### Process Model

We will use the Unified Process as in the textbook.

### Methods Tools and Techniques

* **Language**: The primary project language will be Python, selected for its abundance of open source libraries.  
* **Diagrams**: Diagrams will follow the standard for UML.  
* **Source control**: Git and GitHub will be used for source control.  
* **Issue tracking**: GitHub Issues will be used to flag and close issues.

### Infrastructure Plan

Students will use a combination of their own laptops, their own operating systems, and collaborate through GitHub. Since Python was selected as the language and is interpreted, there will be no need for a compiler standard.

### Product Acceptance Plan

The client accepts the product after:

* It is handed in on D2L and meets the questions asked of the students.

## Supporting Process Plans

### Configuration Management Plan

All files are stored in the git repository located [here](https://github.com/actellim/ChocAn). We use branches for features, and pull requests for review.

### Testing Plan

Unit tests for classes integration tests for flows and product tests for full scenarios. Each person first tests their code and then tests a teammate code. The git repository owner runs final integration tests.

### Documentation Plan

We deliver the user setup steps, and final report. All docs follow the same format as Appendix F.

### Quality Assurance Plan 

- Peer reviews for all artifacts.   
- When a team member finishes a feature they request another team member to test it via e-mail.  
- The git owner does integration testing and product testing.

### Reviews and Audits Plan

### Problem Resolution Plan

Any major problem is recorded as a GitHub Issue at once. The github owner reads it, assigns it, sets a due date, and tracks to closure.

### Subcontractor Management Plan

Not applicable.

### Process Improvement Plan

We follow the team plan to improve repeatable practices and move toward higher maturity in the next term project. We will keep a record of our processes and lessons learned to iterate on our development process.

## Additional Plans

### Security

A password is needed to perform CRUD operations on the database. Providers login using their provider ID. All roles are limited to the needed actions.

### Training

Training will be given by Vu at delivery. One day is expected. Questions for the first year are supported at no cost.

### Maintenance

The team provides the software as-is, without warranty, with a full apache-2 license. Enhancements will use a separate agreement.

