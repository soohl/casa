<!-- TOC -->

- [1. Object Oriented Design](#1-object-oriented-design)
    - [1.1. Data-Driven](#11-data-driven)
    - [1.2. Event-Driven](#12-event-driven)
    - [1.3. Responsibility-Driven](#13-responsibility-driven)
- [2. Responsibility Driven Design](#2-responsibility-driven-design)
    - [2.1. Single Responsibility Principle (SRP)](#21-single-responsibility-principle-srp)
        - [2.1.1. Information Expert](#211-information-expert)
        - [2.1.2. The Hierarchy](#212-the-hierarchy)
        - [2.1.3. RDD Stereotypes](#213-rdd-stereotypes)
        - [2.1.4. Domain Model에 추가하기](#214-domain-model에-추가하기)

<!-- /TOC -->

# 1. Object Oriented Design
Object oriented design을 시작할때에는 크게 3가지의 접근 방식이 있다. 
1. Data-Driven
2. Event-Driven
3. Responsibility-Driven

이 3가지의 방법들은 개발에 앞서 디자인 단계부터 차이점을 보인다. 예를 들어
말`horse`이 등장하는 소프트웨어를 만든다고 가정해보자. 

## 1.1. Data-Driven
Data-Driven 접근법은 Object인 말을 `Property`와 `action`으로 분류해서 접근한다. 
* **Property**:
    1. Speed - 말의 속도
    2. Color - 말의 색
    3. Height - 말의 높이
* **Action**:
    1. ride() - 사람 태우기
    2. eat() - 음식 먹기
    3. run() - 마구 뛰기

## 1.2. Event-Driven
Event-Driven 접근법은 말의 상태 `status` 와 그에 따른 반응 `response`로 분류해서
접근한다.
* **상태** -> **반응**
* Hungry (배고픔) -> eat() 먹는다.
* Spur (발차기) -> move() 움직인다.
* Load (싣기) -> carry() 짊어진다.

## 1.3. Responsibility-Driven
Responsibility-Driven 접근법은 말이 우리 소프트웨어에서 가지는 책임`responsibility`로 분류해서 접근한다. Object의 본질보다는 Object의 존재이유 (실존)에 대해 더욱 집중하는 접근법이라 할 수 있겠다. 현재로서는 소프트웨어 디자인에 있어서 사람들이 가장 선호하는 `state of art design principle`이라고 한다. 

**던져야 하는 질문**
* 말 object는 우리의 소프트웨어에서 어떠한 책임을 가지고 있는가?
* 우리는 무슨 목적의 소프트웨어를 만들고 싶은가? (심, 게임?)
* 우리의 소프트웨어는 말에 대해서 얼마나 알고 있어야 하는가? 

**예시**
* 우리는 말을 관리하는 소프트웨어를 만들겠다. 
* 우선 말의 상태를 기록하기 위해 말의 고유 번호, 음식 섭취량, 몸무게, 소유자 
이름 등등의 정보를 보관해야 한다. 
* 매일 말의 상태를 점검하기 위해 `generateSummary()`라는 메소드를 통해 
말들의 상태를 요약해주는 기능이 필요하다. 
* 말의 속도 등은 소프트웨어가 알 필요가 없을것 같다. 

# 2. Responsibility Driven Design
## 2.1. Single Responsibility Principle (SRP)
Responsibility driven 디자인 중에서도 SRP는 각 class가 하나의`single` 책임`responsibility`만 을 가져야 한다는 개념이다. 여기서 `responsibility`는 method를 뜻하는 것이 아니라 역할, 책임이라는 추상적인 개념이다. 한 class는 여전히 여러개의 method을 가질 수 있다. 오해하지 말자. 예를 들어 학생의 점수를 pdf로 만드는 프로그램을 만들어본다고 가정해보자. 

**잘못된 방식**
* Student class에서 성적을 담은 `arrayList`와 `pdfFormat()`이라는 method을 통해서 pdf를 만든다.
* 다음의 방법이 잘못된 이유는 student class 혼자 학생들의 성적을 담고 있어야 하는 책임뿐만 아니라 성적을 pdf로 만들어야하는 책임 또한 지고 있기 때문이다. 하나의 class가 두개의 `responsibility`을 가지는 것을 우리는 원치 않는다. 

**올바른 방식**
* Student class는 학생들의 성적만 담고 새로운 `pdfFormatter`라는 class에서 학생의 성적을 가져와서 `pdfFormat()`을 통해서 pdf를 만든다. 
* pdf를 만드는 책임을 지는 별도의 class를 생성하여 student class가 져야할 책임을 위임하였다. 이를 통해서 하나의 class는 하나의 `responsibility`만을 가지게 되었다. 

> Each class should have a single responsibility or a single reason to change. 

### 2.1.1. Information Expert
Information Expert는 특정한 class에 책임을 부여할 떄 그 class가 부여하고자 하는 책임을 다 할 수 있을 만큼 충분한 정보`data`를 지니고 있어야 한다는 개념이다. 즉, class가 특정한 책임을 지닐 수 있는 능력 (정보의 접근성등)이 충분할 경우에만 책임을 부여하여야한다는 것이다. 간단하게 말해서 감당할 수 있는 능력이되는 class에게 그 책임을 부여해야한다는 뜻이다. 

### 2.1.2. The Hierarchy
RDD에서 통용되는 해석들이다. 

* An application = a set of interacting objects
* An object = an implementation of one or more roles
* A role = a set of related responsibilities
* A responsibility = an obligation to do a task or know information or decide something
* A collaboration = an interaction of objects or roles (or both)
* A contract = an agreement outlining the terms of a collaboration
> Object Design by Rebecca Wirfs-Brock 참조

### 2.1.3. RDD Stereotypes
책임의 종류에 따라 각 class를 일련의 직업으로 분류할 수 있다. 물론 각 class가 하나의 직업만을 가질 필요는 없다. 예로 한 class가 `information holde`r와 `Serice Provider`의 역할을 동시에 가질 수 있다. 다만 하나의 class가 너무 많은 역할을 하게 되면 문제가 있다.  

* Information Holder – to know things
* Service Provider – to do things
* Structurer – to organize things
* Interfacer – to adapt one part of a system to another
* Coordinator – to decide things using set, non-adaptive logic
* Controller – to decide things using adaptive logic

`Coordinato`r와 `Controller`의 차이점은 `Coordinator`는 정해진 룰에 따라 같은 작업을 반복하는 반면에 `Controller`는 상황에 따라 다르게 반응 할 수 있다. `Coordinator`는 static 알고리즘을, `Controller`는 dynamic 알고리즘을 사용한다고 보면 될것이다. 예로 `Coordinator`가 정해진 시간에 따라 신호등을 컨트롤 한다면 `Controller`는 교통량에 따라 신호등을 컨트롤 한다.

**ATM 예시:**

* Customer – mainly responsible for knowing things about a customer (name, balance, account number, etc) – Information Holder
* TransactionProcessor – mainly responsible for processing deposits and withdrawals from the machine – Service Provider
* AtmMachine – responsible for organizing the objects for the different parts of the ATM into a cohesive abstraction – Structurer
* DataStore – responsible for interfacing the ATM system to the bank’s database provider -  Interfacer 
* FrontController – retrieves messages from ATM and relays them to correct part of system for processing – Coordinator 
* AdaptiveMessageQueue – obtains messages from the bank network.  routes to other parts of the system taking into account current workload and network bandwidth –Controller 

### 2.1.4. Domain Model에 추가하기
* Class의 `stereotype`은 UML class 이름 위에 <<...>> 안에 표기하면 된다.
* 한 class가 여러개의 `stereotype`을 가진다면 가장 중요한 `stereotype` 하나만을 표기한다. 