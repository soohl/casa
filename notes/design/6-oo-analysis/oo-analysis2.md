<!-- TOC -->

- [1. OO Analysis 2](#1-oo-analysis-2)
- [2. Domain Models](#2-domain-models)
    - [2.1. Step 1 - Brainstorming](#21-step-1---brainstorming)
    - [2.2. Step 2 - Filtering](#22-step-2---filtering)
    - [2.3. Step 3 - Draw domain model](#23-step-3---draw-domain-model)
        - [2.3.1. Multiplicity / Cardinality Constraint](#231-multiplicity--cardinality-constraint)
        - [2.3.2. Caution](#232-caution)
        - [2.3.3. Where do this domain model sit?](#233-where-do-this-domain-model-sit)

<!-- /TOC -->

# 1. OO Analysis 2 
# 2. Domain Models 
*Focus on what is important to the customer – NOT what is important to the programmer!*

**Domain Model (Vocabulary)**
* Something that the customer understands (e.g.assignment, course)
* Stakeholders may use different terms in different parts of the company to mean the same thing
* We need a standard agreed-upon vocabulary that is not **ambiguous**.

## 2.1. Step 1 - Brainstorming
* Team generates a lot of possible objects
* Noun Analysis (write all the noun)
* Domain Analysis (e.g. monopoly game --> board game --> list everything from board game like `piece`, `board`, `token`)

## 2.2. Step 2 - Filtering
**The customer should recognize every noun that we are selecting**
* Need to reduce this big list down to candidate objects that we think are in the customer domain
**Look for**
* **Synonyms** - mean same thing
* **Attributes** - just a simple number, string
* **Implementation** - represent design decision, not customer domain (networking, ds etc)
* **User interface** - represent UI ideas (windows, screens etc)

## 2.3. Step 3 - Draw domain model
* Candidate classes with their attributes and methods
* No visibility marking (private/public)
* No parameters or return types
* No types of instance data
* Provide `basic boxes`, `associations` and `cardinality constraints`
```
|---------|
| Name    |
|---------|
| ATTR    | <- Things I know
|         |
|         |
|---------|
| RESP    | <- Things I do
|         |
|---------|

Example) 
Association (Relationship)
|---------|             |---------|
| Course  |   Register  | Student |
|---------|     <--     |---------|
| ATTR    | 1..5   1..5 | ATTR    |           
|         | ----------- |         |
|         |             |         |
|---------|             |---------|
| RESP    |             | RESP    |
|         |             |         |              
|---------|             |---------|
```

### 2.3.1. Multiplicity / Cardinality Constraint
* `*` = 0 to infinite
* `1..5` = 1 to 50 (min,max)
* `3` = must be 3
* `0, 3` = 0 or 3
* `0,1` or `0..1` = binary option

### 2.3.2. Caution
* Domain Model != UML Diagram
* Must learn more about the domain itself to program about
* For larger system, concepts may have different meanings and function (e.g. Policy), so we introduce `bounded context` so the domain model can vary between user group.
* Do not develop an application without a domain model
* Do not lose connection between domain model and the code
* Do not try to have a "pure" analysis model (don't change the name)

### 2.3.3. Where do this domain model sit?
In layered architecture, 
* **User Interface** - layout, xml
* **Application** - repository, viewmodel, adapter
* **Domain** - Entity
* **Insfrastructure** - Database
