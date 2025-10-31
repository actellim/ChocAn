---
title: Software Project Management Plan
subtitle: For the ChocAn Project
bibliography: references.bib
---

# Software Project Management Plan

## Overview

### Project Summary

#### Purpose, Scope, and Objectives

The goal is to build ChocAn’s Project, a software product that supports provider terminal and ChocAn database interaction.  
The product will let the client add, edit, and delete the needed records, run the required checks, and produce weekly reports and payment files. *Nort Light Software* will deliver a working product that meets all stated requirements, and ship the product to the client on time. *North Light Software* will produce clear reports and correct totals.

#### Assumptions and Constraints

Constraints include the following:  
* We must meet the deadline and stay within the budget.
* The product must be reliable and easy to maintain.
* The design must allow new features later.
* The user interface must be simple.

#### Project Deliverables

*North Light Software* will deliver a working product, a user guide, technical notes, setup guide, test results, and acceptance record.

#### Schedule and Budget Summary

The workflow estimates are as follows:
* Requirements workflow – 3 weeks, three people, 12h.
* Analysis workflow – 1 week, three people 20h.
* Design workflow – 1 week, three people, 20h.
* Implementation workflow – 1 week, three people, 50h.
* Testing workflow – 1 week, three people, 30h.
* Total 10 weeks and 132h.

#### Evolution of the Project Management Plan

Any change to this plan must be approved by the engineering team, and recorded so the plan stays current.

## Reference Materials

All work will follow the textbook standards for coding documents, testing, and reviews. 

## Definitions and Acronyms

* **ChocAn**: The client company.
* **Client**: the sponsor or user of the system.
* **DataCenter**: the main system that stores records and runs reports.
* **EFT**: electronic funds transfer file for provider payments.
* **UI**: user interface.
* **DB**: database.

## Project Organization

### External Interfaces

All work on this project will be performed by Vu, Kenneth, or Joshua. AI usage will be cited. Questions that can't be solved internally will be escelated to Dr. A. Diyab via e-mail.

### Internal Structure

The engineering team consists of three Lakehead University Engineering students: Kenneth, Vu, and Josh.

### Roles and Responsibilities

Engineering communicates via e-mail if they have questions, keep records current on the git project, and escalate questions to Dr. Diyab via e-mail. Each member is responsible for the quality of their artifacts, and for verifying the quality of other's artifacts prior to submission.

## Managerial Process Plans

### Start up Plan

#### Estimation Plan

Total time to hand-off is 7 weeks in total. Internal time cost is estimated to be 132 hours. These estimates are based on the class project deadline.

#### Staffing Plan

The three engineering students are needed for all 10 weeks, first 5 weeks as analysts and designers, then as developers and testers.

#### Resource Acquisition Plan

All tools and machines are available. The product will be delivered as source code, and the client will be expected to run it in their environment.

#### Project Staff Training Plan

The engineers will be responsible for **first** reviewing the textbook and **then** consulting AI with any follow-up questions about their roles.

### Work Plan

#### Work Activities and Schedule Allocation

| Week | Activity |
|---|---|
| Week 1-3 | gather and inspect requirements, meet with the client, define group setup, and confirm scope. |
| Weeks 4 | build analysis artifacts and inspect them, then get client approval. |
| Weeks 5 | build design artifacts and inspect them. |
| Weeks 6-7 | begin implementation by writing tests, then implement classes, integrate them, write docs, and do the final inspection. |

#### Resource Allocation

Each member works on assigned artifacts. Twice-weekly we will conduct a brief stand up before or after class to track progress and blockers. Scope changes will be confirmed with the clinet after the stand up. Documentation will be kept up to date in the `docs/` folder of the project's git repository.

#### Budget Allocation

|Activity|Time-Cost|
|---|---|
|Requirements| 12h |
|Analysis| 20h |
|Design| 20h |
|Implementation| 50h |
| Testing| 30h |
| Total | 132h |

### Control Plan

Any change that affects time or budget must be approved by the engineering team and recorded. Each person tests another person's work to keep quality. Any major problems will be communicated with the engineering team via e-mail as soon as possible.

### Risk Management Plan

There is currently no existing product to compare to, so we plan for strong testing.
The ChocAn providers may have a limited technical background, so screens are to be kept simple, and frequently reviewed for simplicity.
There may be possible design faults, so we review the designs often, and write tests early.
There is a possibility of tablet or reader failure, so we keep spares on hand to give to providers to minimize downtime.
Performance risk is low, due to small project size, but we will monitor response time. The choice of an interprited language marginally increases this risk.

### Project Close out Plan

*North Light Software* will submit our project, and all artifacts, on D2L on, or before, the due dates; or communicate with the client any delays in advance of the deadline. *North Light Software* will give the client the product, user guide, test results, and recieve an acceptance note. *North Light Software* will then collect lessons learned.

## Technical Process Plans

### Process Model

We will use the Unified Process as described in the textbook[@Schach2010].

### Methods Tools and Techniques

Workflows will be performed as described in *The Unified Process*. The Product will be impletemed in Python. Diagrams will follow typical UML structure. Git and GitHub will be used in tandem for source control. GitHub Issues will be utilized to flag and close issues.

### Infrastructure Plan

Students will use a combination of their own laptops, their own operating systems, and collaborate through GitHub. 

### Product Acceptance Plan

The client accepts the product after it is handed in on D2L and meets the requirements outlined in the assignment questions.

## Supporting Process Plans

### Configuration Management Plan

All files are stored in the git repository located [here](https://github.com/actellim/ChocAn). We use branches for features, and pull requests for review.

### Testing Plan

Unit tests for classes integration tests for flows and product tests for full scenarios. Each person first tests their code and then tests a teammate code. The git repository owner runs final integration tests.

### Documentation Plan

We deliver the user any requested documentation or artifacts. All documents are to follow the same format as outlined in *The Unified Process*[@Schach2010].

### Quality Assurance Plan 

Engineering should conduct peer reviews for all artifacts: when a team member finishes a feature, they request another team member to test it via e-mail. The git owner will be responsible for integration, and product testing.

### Reviews and Audits Plan

Not applicable at this time.

### Problem Resolution Plan

Any major problem is recorded as a GitHub Issue at once. The github owner reads it, assigns it, sets a due date, and tracks to closure.

### Subcontractor Management Plan

Not applicable to this project.

### Process Improvement Plan

We follow the team plan to improve repeatable practices and move toward higher maturity in the next term project. We will keep a record of our processes and lessons learned to iterate on our development process.

## Additional Plans

### Security

A password is needed to perform CRUD operations on the database. Providers login using their provider ID. All roles are limited to the needed actions.

### Training

Training will be given by Vu at delivery. One day is expected. Questions for the first year are supported at no cost.

### Maintenance

The team provides the software as-is, without warranty, with a full apache-2 license. Enhancements will use a separate agreement.

## References
