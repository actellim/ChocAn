## 13: Object Oriented Analysis

- **Object-oriented analysis (OOA):** a semiformal analysis technique, of which *The Unified Process* is the most accepted.
- How to perform *Object-Oriented Analysis*:
	1. **Iterate** until all *entity classes* have been extracted:
		1. Perform *functional modeling*.
		2. Perform *entity class modeling*.
		3. Perform *dynamic modeling*.
	2. Extract *boundary* and *control* classes.
	3. Refine the *use-cases*.
	4. Perform *use-case realization*.

## Learning Objectives

- Perform the analysis workflow.
- Extract the boundary, control, and entity classes.
- Perform functional modeling.
- Perform class Modeling.
- Perform dynamic modeling.
- Perform use-case realization.

## 13.1 The Analysis Workflow

- **analysis workflow:** to obtain a deeper understanding of the requirements, and to describe them in such a way that the resulting design and implementation is easy to maintain.
- **entity class:** models information that is long lived.
- **boundary class**: models an interaction between the software and its actors, and is generally associated with input and output.
- **control class:** models complex computations and algorithms.
- **stereotypes** are extensions of UML, of which entity, boundary, and control classes are.
- The aim of the analysis workflow in *The Unified Process* is to extract *entity, boundary, and control classes* from the *Use Cases* developed in the requirements workflow.

## 13.2 Extracting the Entity Classes

- A **scenario** is an instance of a use case.
1. **functional modeling** presents *scenarios* of all the *use cases*.
2. **entity class modeling:**
	- Determine the *entity classes* and their attributes.
	- Determine the *interrelationships* and *interactions* between entity classes.
	- Present this as a *class diagram*.
3. **Dynamic Modeling:** Determine the operations performed by or on each entity class or subclass, use this to build a state chart.
4. *Iterate*.

## 13.3 Object-Oriented Analysis

- We iterate through *use cases* and build classes from each case.

## 13.4 Functional Modeling

- **use case:** describes the interaction between the product to be constructed and the external users of the product.
- **actors:** users of a product.
- **normal scenario:** a set of interactions between users and the software the corresponds to the way we understand the software should be used.
- **exception scenario:** depicts what happens when the users misuse the software.
- **responsibility-driven design:** requires us to assign a responsibility for each action in the software.
- The goal of functional modeling is to extract as many *normal scenarios* and *exception scenarios* from a specific use case as possible.
- During functional modeling it is *critical* to assign responsibility for each action.
- Actions should use an active voice and use cases should be written from the user's perspective.

## 13.5 Entity Class Modeling

- Only classes and attributes are extracted here, *not* methods.
- Extracting the minimum number of classes possible is ideal, as class reduction is harder than class addition.
- Can be done via *noun extraction* or *CRC Cards*.

### 13.5.1 Noun Extraction

- **noun-extraction method:** a way to extract potential entity classes and refine them into actual entity classes.
	1. Describe the software *use case* in a single paragraph.
	2. Identify the *nouns*, they become *candidate entity classes*.
	- Ignore nouns *outside* the boundary of the problem.
	- Ignore **abstract nouns** -- these are likely to become attributes.
- This is a good time to draft a **class diagram:** UML diagram showing classes, their methods, and their relationships.
- *Noun-extraction* should be thought of only as a starting point, as it can often miss more abstract classes.

### 13.5.2 CRC Cards

- **class-responsibility-collaboration (CRC) cards** show the name of the class, it's responsibility, and a list of other classes it invokes to achieve it.
	- Also contains the attributes and methods rather than responsibility.
- *CRC* cards can be used effectively by emulating them: *using them to act out the responsibilities of each class*.
- *CRC* cards become more effective during later iterations of the analysis process.

## 13.6 Dynamic Modeling

- A **statechart** is a description of software that is similar to a finite state machine.
	- *current state* and *event* and *predicate* -> *next state*
	- Not meant to be a complete representation.
	- *state, event, predicate* are distributed over the UML diagram.
- The goal of dynamic modeling is to produce a *state chart* by generalizing across the *normal and exception scenario* models from all *use cases*.

## 13.7 The Test Workflow

- The **test workflow** resumes at this point to review the analysis workflow.
	1. Analyze each class using CRC cards and modeling the interactions between them.
	2. Elimination of **God Classes** (classes that expose too much information and have too much control) and other anti-patterns is the key element of the test workflow.
	3. Another key element of the test workflow is to detect missing classes.
- We also need to ensure that we update the UML diagrams at this point if any classes are or were modified.

## 13.8 Extracting the Boundary and Control Classes

- *Boundary classes* control input screens, output screens, and reports.
- *Control classes* control all non-trivial calculations.

## 13.9 The Initial Functional Model

- The goal of the initial *boundary* class modeling is to extract the *scenarios* by modeling the associated *use cases*.

## 13.10 The Initial Class Diagram

- A good place to start here is with *noun extraction*.
- A **superclass** occurs when two or more classes have identical functions, at which point their *use cases* may be merged.
- If a *superclass* is detected it may be a good time to *backtrack*.
- May need to **backtrack** to an earlier version and find a better way of performing a step of design then to continue here.

## 13.11 The Initial Dynamic Model

- The *third step* in object-oriented analysis.
- The goal of drawing up the *initial dynamic model* is to develop a complete model of the project.
- We say that **events** cause **transitions** between *states*.
	- It should include all possible states, events, and transitions.

## 13.12 Revising the Entity Classes

- Artifacts drafted to this point: functional model, class diagram, and the dynamic model.
- At this point the models should be reviewed and checked for potentially missing data or steps.

## 13.13 Extracting the Boundary Classes

- Determine the number of different screens, and ensure that a class exists for managing each.

## 13.14 Extracting the Control Classes

- Any lengthy calculations or complex operations should be assigned to their own control class.

## 13.15 Use-Case Realization

- **Definitions:**
	- A **use-case realization** is the process of extending and refining the use cases.
		- By *realize* we mean accomplish.
		- This is the next step in *The Unified Process*.
	- An **interaction, sequence, or communication diagram** depicts the realization of a specific scenario of a use case.
	- A **flow of events** diagram is used to simplify the communication diagram so they can be understood by clients.
- During the *use-case realization* the *use-cases*, *class diagrams*, *scenarios*, *communication diagrams*, and *sequence diagrams* are all updated in an iterative manner (when a realization is made about one while modeling another, we circle back and update it with the new insight):
	1. For each *use-case* we derive multiple *scenarios*.
	2. We then derive *communication diagrams* from each *scenario*.
	3. For each *communication diagram* we derive a *flow of events*.
	4. From the *flow of events* for each *scenario* we draw a UML sequence diagram.

## 13.16 Incrementing the Class Diagram

- At this point the *Use-Cases* have all been realized.
- The goal of this step is to combine the updated relationships between the classes into a class diagram for the entire project.

## 13.17 The Test Workflow

- Here we again inspect the artifacts to ensure they are consistent with themselves.

## 13.18 The Specification Document in The Unified Process

- The **specification document** is the primary final output of the analysis workflow.
	- In *The Unified Process* it is contained in all the artifacts to this point.
- The total of the artifacts at this point is what constitutes a contract between the user and the software agency.
- At this point the user effectively signs off after inspecting the artifacts and the process becomes internal until the software artifact is produced, short of a major fault.

## 13.19 More on Actors and Use Cases

- A **role** is a way in which an individual or agent can interact with the software product.
	- Not all *roles* are different users, which can make extracting the *use-cases* tricky.
	- Users can play multiple *roles* across different (or even sometimes the same) *use-case(s)*.
- We should list all *roles*, then group them by *user* and *actor*.

## 13.21 Metrics for the Analysis Workflow

- The five metrics to track are: size, cost, duration, effort, quality.
	- These can be extracted by examining the UML diagrams and other artifacts.
	- The number of pages of UML can be used to compare different projects.
	- The number and rate of faults would be another important metric to examine at this point.

## 13.22 Challenges for the Object-Oriented Analysis Workflow

- Difficult to separate from the design workflow.
	- Assigning methods to classes should be delayed until the design workflow.

## Reasons for Analysis

- Reasons for analysis: Need to build a SPMP, build a contract.
- Translate into more technical language.
- This involves drawing UML diagrams.
- Main distinction between classical and oop is the diagrams.
- Iterative in nature.
- Three classes:
    - Entity
    - Boundry
    - Control
- **Noun Extraction**
- **Functional Modeling**
- Edge Cases/Exception Scenarios
- CRC Cards
    - Class name
    - Functionality
    - List of classes it collaborates with.
    - Generally part of CASE tools.
    - A component of responsibility driven design.
    - When used properly help to detect missing/incorrect items.
    - *Testable.*
- **Statechart**
    - Again, very interative design process.
- **Boundry Class**
    - Interaction between product and environment.
    - Associated with inputs and outputs.

