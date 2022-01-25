<!-- TOC -->

- [1. Team Development and Source Control](#1-team-development-and-source-control)
- [2. Configuration Management](#2-configuration-management)
    - [2.1. Configuration Problems](#21-configuration-problems)
    - [2.2. Configuration Decisions](#22-configuration-decisions)
- [3. Git](#3-git)
    - [3.1. When is the manual merge required and not?](#31-when-is-the-manual-merge-required-and-not)
    - [3.2. How to avoid manual merge?](#32-how-to-avoid-manual-merge)
- [4. Configuration & Build Tools](#4-configuration--build-tools)

<!-- /TOC -->

# 1. Team Development and Source Control

# 2. Configuration Management 
* Planning
* Identification
* Control
* Status Accounting
* Evaluation
* Release Management and Delivery

## 2.1. Configuration Problems
**Problem**

"How to allow many developers to work on your code at the same time?"

**Solution**
* One Person - One File
* Email Notification
* Token Based (coke can)
* **Source Control System** (CVS, Subversion, Git)

## 2.2. Configuration Decisions
* What do we control?
* When do we start to control it?
* How do we stay in sync?

# 3. Git
## 3.1. When is the manual merge required and not? 
1. If Bob and Sally **work on different file** : `auto-merge`
2. If Bob and Sally **work on different part of the file**: `auto-merge`
3. If Bob and Sally **work on same part of files**: `manual-merge`

## 3.2. How to avoid manual merge?
1. Work on different lines of code
2. Start with fresh code everytime (`git clone`)

# 4. Configuration & Build Tools

* **Ant** : Build Only
* **Maven**: Project Management + Dependency Management and build integrated
* **Gradle**: DSL for builds based upon Groovy
* **Cruise Control**: automatic builds and integration 
* **Jenkins / Travis CI**: automated and management

**Build file**

Instructions for building all or part of an application. This includes everything needed to successfully create the app and deploy it. 

**Target**

A high-level goal of the build. This might be: compile the code, make a jar, create the documentation, etc. In Gradle, targets are called tasks. 

**Convention**: Gradle
VS
**Configuration**: Ant, Maven



