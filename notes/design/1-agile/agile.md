
<!-- TOC -->

- [1. Agile Development](#1-agile-development)
    - [1.1. Why Software project fails?](#11-why-software-project-fails)
    - [1.2. Why Software project is hard to be succesful?](#12-why-software-project-is-hard-to-be-succesful)
- [2. Software Development Life Cycle (SDLC)](#2-software-development-life-cycle-sdlc)
    - [2.1. Waterfall model](#21-waterfall-model)
        - [2.1.1. Why waterfall model is bad?](#211-why-waterfall-model-is-bad)
        - [2.1.2. Waterfall VS Agile Development](#212-waterfall-vs-agile-development)
- [3. Methods of software delivery](#3-methods-of-software-delivery)
    - [3.1. Scope-Boxed (traditional)](#31-scope-boxed-traditional)
    - [3.2. Time-Boxed (agile)](#32-time-boxed-agile)
        - [3.2.1. Iterative Delivery](#321-iterative-delivery)
- [4. SCRUM (agile processes)](#4-scrum-agile-processes)
    - [4.1. SCRUM Illustration](#41-scrum-illustration)
    - [4.2. Kanban Board](#42-kanban-board)
    - [4.3. Burn down chart](#43-burn-down-chart)

<!-- /TOC -->

# 1. Agile Development

## 1.1. Why Software project fails?
**Adjustable elements in software project**
* Resources
* Schedule
* Features
* Quality

## 1.2. Why Software project is hard to be succesful?
For real world engineering, change of plan in the middle of the project is **impossible**.

*Example)* building construction

But, software development is **indefinitely mealuable**. 

# 2. Software Development Life Cycle (SDLC)

## 2.1. Waterfall model 
Waterfall model was a conceptual model used to plan software development project. 

```
//// Waterfall Model ////
Requirements
    ㄴ Design
        ㄴ Implementation
            ㄴ Verification
                ㄴ Maintenance
```

### 2.1.1. Why waterfall model is bad?
* Implementation problem
* Customer change plan
* **Does not produce the product until the end (no demo)**

### 2.1.2. Waterfall VS Agile Development
**Waterfall** is building a pyramid from the bottom to top. The pyramid is not produced until the very end. 

**Agile** is building a very small pyramid and adding on to it. There is always a pyramid to show (demo). There is a continuous working software delivery.

# 3. Methods of software delivery
## 3.1. Scope-Boxed (traditional)
```
    JAN   FEB   MAR  . . . 
T1: -------
T2:      --------     
T3:          -------- <---->
T4:                    slip 
```
When the product is not ready to be demo with all the features, the schedule will be slipped.

## 3.2. Time-Boxed (agile)
```
                   DEMO 1
    JAN   FEB   MAR  |
T1: -------          |
T2:      --------    |
T3:          --------|
T4:                30,MAR
```
Whether or not all features of the product is ready, the product will be out for demo as scheduled, **but may not contain all features.**

> Time Boxed is a more princpled delivery method. Time boxed method can also be used for meeting time (fixed meeting time) and other stuffs. 

### 3.2.1. Iterative Delivery
* Project is divided in pices called iterations.
* At end of iteration something is delivered
* No schedule slip (timeboxing as opposed to scopeboxing)
* Each iteration nominally 4 weeks
* Each iteration does varying amounts of analysis, design, implementation and testing

# 4. SCRUM (agile processes)
**Agile processes**
* **SCRUM** (project management)
* Extreme Programming (XP)
* EVO (requirements focused)
* RUP Dx (complete system)

**SCRUM**
* Focuses mainly on management of software product development
* Timeboxed iteration called **sprints**
* Project planned through use of 2 spreadsheets (product and sprint)
* Daily Meeting 
* Each sprint ends with "ready" deliverable

## 4.1. SCRUM Illustration
```
 FEATURE  
|-------| } *Product Backlog* (by customer, product owner)
|-------| }     1. PBI   ---> Highest priority
|-------| }     2. ...   ---> Lowest priority
    |           3. ...   ---> stretch goal
    |           4. ...   ---> No chance
    |
    |                    *1 feature per 1 sprint*
    |--------> |---| 1. Breakdown to features by developer
               |---| 2. Implement features (daily meeting)
               |---|                |
                                    |         *RELEASE*
                                    |------> |--DEMO--| 
                                        
                                        New demo for each sprint
```
## 4.2. Kanban Board
```
|---|  |---|  |---|  |---| 
|   |  |   |  |   |  |   |
|   |  |   |  |   |  |   |
|   |  |   |  |   |  |   |
|---|  |---|  |---|  |---| 
(PBI)  (TASK) (IN)   (DONE)
              (PROGRESS)
```
**Daily meeting about tasks**
1. I've done ...
2. I will do ...
3. I have problems ...

## 4.3. Burn down chart
* Estimate schedule of each sprint
```
Story Points
| \
|  *
|   \
|    *  
|     \
|      \  estimate
|-----------------
  (1)  (2)  (3)
    Time (Sprint)
```
