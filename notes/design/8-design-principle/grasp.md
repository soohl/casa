<!-- TOC -->

- [1. Design Principle을 배우기 전에 명심해야 하는 점](#1-design-principle을-배우기-전에-명심해야-하는-점)
- [2. Coupling (커플링)](#2-coupling-커플링)
    - [2.1. 절대 하지 말것!](#21-절대-하지-말것)
    - [2.2. 되도록이면 피해야하는 것!](#22-되도록이면-피해야하는-것)
    - [2.3. 가능한 것!](#23-가능한-것)
- [3. Cohesion (코히션)](#3-cohesion-코히션)
    - [3.1. 되도록이면 피할 것!](#31-되도록이면-피할-것)
    - [3.2. 가능한 것!](#32-가능한-것)
- [4. Coupling과 Cohesion은 상충 Tradeoff 관계?](#4-coupling과-cohesion은-상충-tradeoff-관계)
        - [4.0.1. Minimum Coupling == Minimum Cohesion](#401-minimum-coupling--minimum-cohesion)
        - [4.0.2. Maximum Cohesion == Maximum Coupling](#402-maximum-cohesion--maximum-coupling)
- [5. GRASP 디자인의 목표](#5-grasp-디자인의-목표)
- [6. GRASP 디자인에서 피해야하는 것들](#6-grasp-디자인에서-피해야하는-것들)
- [7. GRASP 디자인의 핵심](#7-grasp-디자인의-핵심)
    - [7.1. Low Coupling](#71-low-coupling)
        - [7.1.1. Low coupling Example](#711-low-coupling-example)
            - [7.1.1.1. Option 1 - Register](#7111-option-1---register)
            - [7.1.1.2. Option 2 - Sale](#7112-option-2---sale)
        - [7.1.2. Coupling은 무조건 나쁜것인가?](#712-coupling은-무조건-나쁜것인가)
    - [7.2. High Cohesion](#72-high-cohesion)
        - [7.2.1. High Cohesion Example](#721-high-cohesion-example)
            - [7.2.1.1. Class 후보들](#7211-class-후보들)
        - [7.2.2. 만약 정보가 다수의 class로 흩어져 있는 경우](#722-만약-정보가-다수의-class로-흩어져-있는-경우)
    - [7.3. Creator (창조자)](#73-creator-창조자)
        - [7.3.1. Assign B to create class A if: (B가 A를 생성해야 하는 경우)](#731-assign-b-to-create-class-a-if-b가-a를-생성해야-하는-경우)
        - [7.3.2. Creator Example](#732-creator-example)
            - [7.3.2.1. Who is responsible for creating a lineItem?](#7321-who-is-responsible-for-creating-a-lineitem)
    - [7.4. Information Expert (정보 전문가)](#74-information-expert-정보-전문가)
        - [7.4.1. Information expert Example](#741-information-expert-example)
            - [7.4.1.1. Who is responsible for knowing the grand total of a sales?](#7411-who-is-responsible-for-knowing-the-grand-total-of-a-sales)
            - [7.4.1.2. Who is responsible for knowing the sub total of a sales?](#7412-who-is-responsible-for-knowing-the-sub-total-of-a-sales)
    - [7.5. Controller (컨트롤러)](#75-controller-컨트롤러)
        - [7.5.1. Controller의 책임](#751-controller의-책임)
        - [7.5.2. Controller의 종류](#752-controller의-종류)
            - [7.5.2.1. Façade Controller](#7521-façade-controller)
            - [7.5.2.2. Use Case Controller](#7522-use-case-controller)
        - [7.5.3. Controller을 사용할떄 주의할 점 – Bloated Controllers (부풀어 오른 controller)](#753-controller을-사용할떄-주의할-점--bloated-controllers-부풀어-오른-controller)
            - [7.5.3.1. 부불어 오른 controller을 고치려면](#7531-부불어-오른-controller을-고치려면)
    - [7.6. Polymorphism](#76-polymorphism)
    - [7.7. Pure Fabrication](#77-pure-fabrication)
    - [7.8. Indirection](#78-indirection)
    - [7.9. Protected Variations](#79-protected-variations)

<!-- /TOC -->

# 1. Design Principle을 배우기 전에 명심해야 하는 점
* 우리가 배우고자 하는 것은 Principle이다. Rule이 아니다. 
* 만약 principle을 따르지 않을 정당한 이유가 있다면 따르지 않아도 된다. Principle을 따르기 위해 쉬운것을 어렵게 만드는 짓은 하지 말자. 

>GRASP 디자인에서 가장 중요한 principle은 "Low coupling, High cohesion"이다. `Coupling`과 `Cohesion`에 대해서 알아보자. 

# 2. Coupling (커플링)
* `Coupling`이란 "한 class가 다른 class에 대해서 어느정도 알아야하는가"에 대한 척도이다. 한 마디로 각 class가 다른 class로 부터 얼마나 독립적으로 작동하는가에 대한 개념이다. 
* `Low Coupling`은 "한 class가 다른 class에 대한 **최소한**의 정보로도 작동하는", 즉 의존도가 낮은`low`상태의 class 디자인이다. 
* `High Coupling`은 "한 class가 다른 class에 대한 정보를 **불필요하게 많이** 알고 있어야 작동하는", 즉 의존도가 높은`high`상태의 class 디자인이다.
* 우리의 목표는 **low coupling**, 즉 각 class가 다른 class에 가지는 의존도를 최소화하는 것이다.

## 2.1. 절대 하지 말것!
* Content - one class modifies another (branch into middle of routine, modifies code)

## 2.2. 되도록이면 피해야하는 것!
* Common - share common (global) data
* Control - use a return code to control a different method

## 2.3. 가능한 것!
* Stamp / Data - passing complex data or structures between modules 
* Uncupled - no relationship between class

# 3. Cohesion (코히션)
* `Cohesion`이란 "한 class가 자신이 맡은 책임에 대해서 얼마나 **집중**하고 있는가"에 대한 척도이다.
* `Low Cohesion`은 "한 class가 하나의 집중되는 작업이 아닌 **분산**된 작업을 하고 있는 낮은`low` 응집력을 가진 상태의 class 디자인이다. 
* `High Cohesion`은 "한 class가 분산된 작업이 아닌 하나의 작업에 **집중**하고 있는 높은`low` 응집력을 가진 상태의 class 디자인이다.
* 우리의 목표는 **high cohesion**, 즉 class들을 각각 하나의 작업에 집중시키도록 만들어 응집력을 최대화하는 것이다. 

## 3.1. 되도록이면 피할 것!
* Coincidental - Unrelated functions

## 3.2. 가능한 것!
* Logical - multiple logic sections with ext select
* Temporal - related by phases of an operation
* Procedural - required ordering of tasks
* Communicational - operates on same data set
* Functional - all essential elements for a single funciton are in same module

# 4. Coupling과 Cohesion은 상충 Tradeoff 관계?
`Coupling`과 `cohesion`에 대한 해석을 보면 이런 생각이 들것이다. "흠 그럼 각 클래스의 의존도를 최소화하고 응집력을 최대화시키면 되는거지? 별거 아닌거 같은데?". 섣부른 생각이다. 두 개념은 보기에는 비슷한 뜻을 가진 것 같지만 알고 보면 상충 `tradeoff` 관계를 나누고 있다. 예시로 살펴보자. 

### 4.0.1. Minimum Coupling == Minimum Cohesion
`minimum coupling`을 가진 디자인은 어떻게 생겼을까? "흠 의존도를 최소화시키면 되니까... 하나의 class에 모든것을 때려 박으면 되겠네!" **그러나!** 모든 작업을 맡고 있는 하나의 class만을 만들게 되면 하나의 class가 모든 일을 하게 된다. 결국, 한class가 분산된 작업을 하게 되고 응집도를 나타내는 `cohesion`은 감소하게 된다. **`Coupling` 지수의 감소는 `cohesion` 지수의 감소로 이어지는 것이다.**

### 4.0.2. Maximum Cohesion == Maximum Coupling
반대로 `maximum cohesion`을 가진 디자인은 어떻게 생겼을까? "흠 응집력을 최대화시키면 되니까... 각 클래스가 하나의 작업 (method)만 가지고 있으면 되겠네!" **그러나!** 각 class가 하나의 작업 (minimum method)만을 가지고 있다면 class의 갯수가 많아질 것이고 결국, 각 class가 다른 class에 대한 정보를 더 많이 알고 있어야 한다. 다른 class의 정보에 접근하는 빈도가 증가하게 되고 의존도를 나타내는 `coupling`은 증가하게 된다. **`Cohesion` 지수의 증가는 `coupling` 지수의 증가로 이어지는 것이다.**

# 5. GRASP 디자인의 목표
* Low coupling
* High cohesion
* Low representational gap (LRG)
* Seperation of concerns

# 6. GRASP 디자인에서 피해야하는 것들
* High coupling
* Low cohesion
* Rigidity -> change of one class affect other class
* Fragility -> fix bug on one class require fix on other class
* Immobility -> ability to reuse the code
* Viscousity (hackability)
* Needless complexity (YAGNI)
* Needless repetition (DRY)
* Opacity (obscure, obtuse) -> clear code > clever code

위에 제시된 규칙들은 GRASP의 핵심이라기보다는 RDD 디자인이 요구하는 전반적인 디자인 특징이라고 할 수 있겠다. 그렇다면 GRASP 디자인의 핵심은 과연 무엇일까? 

# 7. GRASP 디자인의 핵심
GRASP은 General Responsibility Assignment Software Patterns의 약자이다. 해석하면 "일반적 책임 부여의 대한 소프트웨어 패턴"이라고 보면 되겠다. GRASP는 구체적으로 9가지의 핵심 디자인 패턴을 말하고 있다.
* Low coupling
* High cohesion
* Creator
* Information Expert
* Controller
* Polymorphism
* Pure Fabrication
* Indirection
* Protected Variations

## 7.1. Low Coupling
Low coupling은 앞에서도 다룬 내용이다. 그러므로 이 편에서는 low coupling에 대한 예시를 다뤄본다.

### 7.1.1. Low coupling Example
POS기 시스템을 만들어보려고 한다. Payment, Register, Sale, 총 3가지의 class가 사용되어진다. 어떤 class가 Payment의 object을 생성해야 할까?

#### 7.1.1.1. Option 1 - Register
첫번째 옵션은 아래 나와있는 것처럼 register class가 payment object을 생성하는 것이다. 
```
                    :Register                 :Sale
* --- makePayment ---> |                        |
                       | -- create |p:Payment|  |
                       |                        |
                       | --- addPayment(p) ---> |
                       |                        |
```
makePayment() 메소드가 실행되면 Register class가 Payment class의 object을 생성한 뒤 Sale class에게 addPayment()의 parameter를 통해 넘겨주는 구조이다. 

#### 7.1.1.2. Option 2 - Sale
두번째 옵션은 아래 나와있는 것처럼 Sale class가 payment object을 생성하는 것이다. 
```
                    :Register               :Sale
* --- makePayment ---> |                      |
                       | --- makePayment ---> |
                       |                      | -- create |p:Payment|
                       |                      | 
                       |                      | -- addPayment(p) -
                       |                      |                  |
                       |                      | <-----------------
```
첫번째 옵션과는 조금 다른 구조를 하고 있다. makePayment() 메소드가 실행되면 Register class가 자신의 makePayment() 메소드를 실행하고 그러면 Sales class가 스스로 Payment class의 Object를 생성한뒤 스스로에 addPayment() 메소드를 통해서 넘겨주고 있다. 

**두 구조 중에 어느 것이 더 낮은 coupling을 가지고 있을까?** 정답은 2번이다. 왜냐하면 Sales class가 Register class의 addPayment() 메소드에 의존하지 않아도 되기 때문이다. 

### 7.1.2. Coupling은 무조건 나쁜것인가?
무조건 그렇다고는 할 수 없다. 예로 Java standard library에 포함된 Collection이나 String class를 사용하게 되면 coupling을 증가시킨다고 생각할 수 있다. 하지만 이것은 다른 이야기이다. 왜나하면 우리가 standard library에 포함된 class들을 수정modify할 수 **없기** 때문이다. 우리가 low coupling을 이루고자 하는 궁극적인 이유는 각각의 class 변화가 다른 class에 끼치는 영향을 최소화하기 위한 것인데, 만약 그 class가 변화화지 않는다면 coupling에 따른 영향도 크지 않을 것이다. 결국 상황에 따라 영향력이 다르므로 coupling이 무조건 나쁘다고 할 수는 없겠다. 

## 7.2. High Cohesion
High cohesion도 앞에서 다룬 내용이다. Coupling과 마찬가지로 예시와 함께 좀 더 알아보겠다.

### 7.2.1. High Cohesion Example
Checker 게임을 만들어보려고 한다. 우리는 다음과 같은 class를 만들었다. CheckersActivtiy, CheckersGame, Player, Piece, Board. 게임이 돌아가는 전체적인 로직은 다음과 같다. 
{% highlight python %}
while game not over:
    for each player p:
        p takes a turn
{% endhighlight %}
**다음과 같은 상황에서 어떤 클래스가 턴을 넘기는 로직을 관리해야 할까?** 단계적으로 접근해보자. 

1. Analyze what information is required
2. Apply the information expert 
3. Evaluate the choice with coupling and cohesion

#### 7.2.1.1. Class 후보들
* CheckersActivity - UI를 담당하므로 로직에 간섭하지 않아야 한다.
* CheckersGame - facade Controller이므로 로직에 간섭하면 cohesion이 낮아진다.
* Player - 플레이어이다. 턴을 관리하기에 적합할 것 같다.
* Piece - 보드의 말이다. 턴을 관리하기에는 적합하지 않다.
* Board - 보드이다. 턴을 관리하기에 충분한 정보를 담고 있을 것이다. 

### 7.2.2. 만약 정보가 다수의 class로 흩어져 있는 경우
1. If there are partial info experts, choose the dominant one.
2. If all about the equal, consider coupling and cohesion and choose best.
3. If still no clear winner consider future evolution of the application. 

## 7.3. Creator (창조자)
Creator는 "누가 class의 새로운 instance를 만드는데에 책임을 지고 있는가 (who is responsible for creating a new instance of a class)"에 대한 디자인 패턴이다. 소프트웨어를 개발하다보면 이와 관련된 문제를 한번씩을 겪어보았을 것이다. 만약에 창조자에 대한 선제적 고민이 없다면 각 class는 마구잡이로 서로의 instance (object)를 생성하게 되는 사태가 발생한다. 결국, 창조자에 대한 명확한 구분과 이해가 없다면 RDD는 무리이다. 하지만 다행히도 creator 패턴이 제시하는 몇 가지의 룰을 따르면 창조자에 대한 명확한 구분이 가능하다. 

### 7.3.1. Assign B to create class A if: (B가 A를 생성해야 하는 경우)
1. B contains or aggregates A (B가 A를 포함하고 있는 경우) - e.g. game class create player
2. B records A (B가 A를 기록하는 경우)
3. B closely uses A (B가 A를 자주 사용하는 경우)
4. B has the initilizaing data for A (B가 A의 초기값을 담고 있는 경우)

### 7.3.2. Creator Example 
룰만 봐서는 이해하기 쉽지 않다. 예시로 알아보자. 현재 3개의 class가 다음과 같은 관계를 맺고 있다.  
```
|  Sales  |         |  lineItem  |       |  productSpec  |
|---------| 1  1..* |------------| *   1 |---------------|
| * Date  | ------- | * quantity | ----- | * Description |
| * Time  |         |            |       | * price       |
|---------|         |------------|       | * itemId      |
                                         |---------------|
```
#### 7.3.2.1. Who is responsible for creating a lineItem?
Sales가 lineItem의 instance를 만들어야 한다. Sales가 여러개의 lineItem을 포함contain하므로 Sales가 lineItem의 창조자가 되어야 한다. 


## 7.4. Information Expert (정보 전문가)
Information expert에 대해서는 전편에서 짧게 다루어 보았다. 핵심은 "책임을 질 수 있는 만큼의 정보를 가진 class에게 그 책임을 지게 하는 것"이다 (Assign a responsibility to the class that has the information necessory to fulfill the responsibility). 

### 7.4.1. Information expert Example
앞에 나온 예시와 같은 상황이다.  
```
|  Sales  |         |  lineItem  |       |  productSpec  |
|---------| 1  1..* |------------| *   1 |---------------|
| * Date  | ------- | * quantity | ----- | * Description |
| * Time  |         |            |       | * price       |
|---------|         |------------|       | * itemId      |
                                         |---------------|
```

#### 7.4.1.1. Who is responsible for knowing the grand total of a sales? 
전체적인 판매 매출을 계산하는 책임은 Sales가 지니고 있어야 한다. 전체 판매 매출을 계산하는데 필요한 정보에 접근 할 수 있는 유일한 class가 sales이기 때문이다. 

#### 7.4.1.2. Who is responsible for knowing the sub total of a sales?
부분적인 판매 매출을 계산하는 책임은 lineItem이 지니고 있어야 한다. Sales 또한 충분한 정보가 있지만 lineItem의 정보량으로도 계산이 가능한 부분이다. Cohesion을 생각하면 lineItem이 적합한 창조자일 것이다.

## 7.5. Controller (컨트롤러)
Controller는 Interactor라고 부르기도 한다. Contoller는 "가장 윗단의 UI가 통신해야 하는 첫번째 class는 누구인가"에 대한 디자인 패턴이다. Front-end의 UI와 밑단에 돌아가는 Back-end의 시스템은 분리되어 작동하는 것이 좋은 디자인이다. 예로 UI을 담당하는 class가 복잡한 계산을 하거나 DB와 통신하는 구조는 절때로 좋은 디자인이라고 할 수 없을 것이다. 그래서 우리에게는 back-end에서 돌아가는 model들과 front-end에서 돌아가는 view가 서로 정보를 주고 받을 수 있도록 해주는 다리brdige가 필요하다. 그 다리 역할을 하는 것이 Controller이다. 참고로 RDD stereotype의 MVC Controller와는 다른 개념이다. 

```
<------Back End------>                                  <----Front End----->
model 1 <----------->|          |------------|          |------------------|  
model 2 <----------->|          |            |          | View + Contoller |
model 3 <----------->* <------> | Controller | <------> | View + Presenter |
database 1 <-------->|          |            |          | View + ViewModel |
database 2 <-------->|          |------------|          |------------------|
```
위 그림처럼 Controller는 UI에서 발생하는 이벤트를 먼저 받고 해당하는 model에게 정보를 넘겨준다. 반대로 model이 변경되면 이를 UI에게 알려서 UI를 실시간으로 업데이트 시켜준다. 

### 7.5.1. Controller의 책임
우리는 Controller 패턴에 따라 별도의 Controller class에게 전체적인 시스템(overall system)을 구성하는 책임과, 발생하는 이벤트event에 따라 생기는 시나리오(Use case)를 구성하는 책임을 부여한다. 대체적으로 Controller는 "(usecase name)Handler", "(usecase name)Coordinator", "(usecase name)Session"등의 이름을 가진다.
* Delegates to other objects work to be done. (다른 object에 할 일를 위임한다)
* Coordinates and controls the activity (activity를 관리한다)
* Does not do a lot of the work itself (자체적으로 많은 일을 하지 않는다)
* UI objects should not have responsibility for fulfilling system events. (UI는 시스템 이벤트에 간섭하지 않는다)
* Keep UI not know anything about the model, and involved in item events. (UI는 model에 접근하지 않아야 한다)
* **Keep UI seperated from buisness logic.** (UI는 비즈니스 로직에 간섭하지 않는다)

### 7.5.2. Controller의 종류 
#### 7.5.2.1. Façade Controller
Façade Controller는 전체 시스템을 상징하는 controller이다. 예로 게임을 만들때 게임에 들어가는 사소한 컴포넌트들을 game이라는 하나의 class가 관리할 수 있다. 여기서 game이 facade controller이다. 
* Represents overall System (전체 시스템을 상징한다)
* Maybe an abstraction of a physical device like the Register, BarCodeScanner, CheckersGame or Robot.
* Suitable when there are not a lot of events to be routed (facade controller를 통해서 가는 이벤트가 많지 않을 경우 적합하다)
* Most methods are “pass-through” to the actual domain classes doing the work (대부분의 메소드가 facade controller안에서 직접적으로, 또는 간접적으로 실행된다)

#### 7.5.2.2. Use Case Controller
Use Case Controller는 facade controller가 사용되기 적합하지 않은 상황에서 사용한다. 하나의 거대한 controller 대신 여러개의 작은 controll를 사용하는 것이 특징이다. 
* Used when the Façade would be too bloated, suffer from too high coupling or too low cohesion
* Best when there are many possible system events
* Allows you to separate the control functions into separate classes. 
* Clean Architecture uses UseCaseInteractors

### 7.5.3. Controller을 사용할떄 주의할 점 – Bloated Controllers (부풀어 오른 controller)
* Using a Façade when there are too many system events.
* Controller is actually performing the system work instead of routing to the correct domain objects.
* Controller has many attributes and maintains significant state information about system.

#### 7.5.3.1. 부불어 오른 controller을 고치려면
* Add more controllers. Change from a Façade controller to use case controllers
* Change the controller so it delegates work to domain objects

## 7.6. Polymorphism
* DO not use a case or switch to handle case where same thing act differently.
* Use polymorphism (using inheritance)

## 7.7. Pure Fabrication
* What object should get responsibility for something to comply with coupling and cohesion, but the info expert solutions are not appropriate?
* Many times, our OO classes model a physical reality (checker, board, square), but sometimes we need to “make up” a class.

*Example)*
* Don’t want to put this in the Sale class because of Cohesion?
* Thus we assign responsibilities to made up class that can be highly cohesive
* We invent a new class, PersistentStorage that has responsibility for Read/Update of objects.
* These kinds of Fabricated classes do not show up in the domain model, only the design models.

## 7.8. Indirection
* How to assign responsibilities to avoid direct coupling between things? 
* How to decouple objects to increase reuse?
* Assign responsibilities to an intermediate object to mediate between components so their services are not coupled.

*Example)*
* TaxAdapterInterface
* PersistentStorage
* Any kind of Wrapper or Adapter that you create is usually trying to help with indirection or reduce coupling.

## 7.9. Protected Variations
* Protected Variations
* How do we design objects so that variations or instability (changes) do not have an impact on other objects?
* Identify points of instability and assign responsibilities to create a stable interface around them.

*Example)*
* Tax interface
* PersistentStorage class

**Two kinds of change:**
* **Variation point**: something that is required by our current design
* **Evolution point**: something that may arise in the future, but is not required now
* We always handle variation points, we handle evolution points if the cost is not too great.