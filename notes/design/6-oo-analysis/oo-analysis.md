<!-- TOC -->

- [1. OO Analysis](#1-oo-analysis)
- [2. User Stories](#2-user-stories)
    - [2.1. WHO - Identify primary users (actors) - context diagram](#21-who---identify-primary-users-actors---context-diagram)
    - [2.2. WHAT - Describe how users will interact - User Stories](#22-what---describe-how-users-will-interact---user-stories)
    - [2.3. Characteristics of good user stories](#23-characteristics-of-good-user-stories)
    - [2.4. Testing user stories](#24-testing-user-stories)
        - [2.4.1. Detail Tasks](#241-detail-tasks)
        - [2.4.2. Acceptance Scenarios](#242-acceptance-scenarios)
        - [2.4.3. Done Done](#243-done-done)
- [3. Story Mapping](#3-story-mapping)
    - [3.1. SPIDR](#31-spidr)

<!-- /TOC -->

# 1. OO Analysis

# 2. User Stories

## 2.1. WHO - Identify primary users (actors) - context diagram
**Types of actors**
* **Primary** - Human computer systems that actually use your system
* **Supporting** - Computer Systems that your system uses, but that do not use your system. 
* **Off-stage** - Stakeholders that care about the system, but that do not use it. 

```
/// Context Diagram ///
---------
|system |*--------- Student   
|       |
|       |*--------- Instructor
|       |
---------
```

## 2.2. WHAT - Describe how users will interact - User Stories
**Standard Format**
* As a `<User type from the context diagram>`,
* I want to `<perform some task that helps me identify a feature of the system>`,
* So that I can `<describe a business or user goal>`.

*Only for primary actor*

## 2.3. Characteristics of good user stories
* `INVEST`
* **I**ndependent - story is independent to each other
* **N**egotiable - do not put implementation lanauge. Keep it general, with no too much detail.
* **V**aluable - provide business value
* **E**stimable - can't be too big, too complex
* **S**mall - break it big story in to small pieces (using epic)
* **T**estable - specify acceptance tests for the story

*One user case per one sprint*

## 2.4. Testing user stories
* List detailed tasks to implement story
* List the acceptance criteria
* List the done done criteria

### 2.4.1. Detail Tasks
Detailed tasks to complete the user story

### 2.4.2. Acceptance Scenarios
*How do we know if the story is working?* (customer focused)

We use Behavior Driven Development (BDD) format:
* **GIVEN:**  some initial conditions
* **WHEN:** the user does something in the system
* **THEN:** the system has some response

*also include when there is invalid input*

### 2.4.3. Done Done
*What is the team’s agreement on work that must be accomplished before this story can be called done by the team?*

*Example)*
* Code is committed to master branch
* Code is reviewed by another development team member
* Test cases are written
* Unit tests and UI automation tasks are written
* Feature is tested for accessibility
* Feature is tagged for analytics

# 3. Story Mapping
* Select MMF(Minimum marketable feature) = MVP = kind of user stories
* Record each process step on a sticky
* For each sticky, apply SPIDR to split. More stickies will be epics.
```
/// MMF = filling out expense report ///
process logic: Login ----> Create New Report ---> Attach Recipt
             { Facebook          ...                  ...
User Stories { Google            ...                  ...
             { Custom            ...                  ...
```

## 3.1. SPIDR
* Spike a story (last choice)
* Paths – look for different paths through a story (like alternative payments)
* Interfaces – web/android/ios may be able to split out by platform
* Data Sources – if data can come from multiple sources, then split on sources
* Rules – If there are a lot of different rules, introduce them slowly over multiple stories