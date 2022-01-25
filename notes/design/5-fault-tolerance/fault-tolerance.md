<!-- TOC -->

- [1. Fault Tolerance System](#1-fault-tolerance-system)
    - [1.1. Digression -- Builder pattern](#11-digression----builder-pattern)
        - [1.1.1. Builder Class](#111-builder-class)
        - [1.1.2. Build User with builder class](#112-build-user-with-builder-class)
- [2. 시스템 에러의 종류](#2-시스템-에러의-종류)
- [3. Fault Tolerance Design Pattern](#3-fault-tolerance-design-pattern)
    - [3.1. Leaky Bucket Pattern](#31-leaky-bucket-pattern)
- [4. Circuit Breaker Pattern](#4-circuit-breaker-pattern)
    - [4.1. Retry Pattern](#41-retry-pattern)
    - [4.2. Timeout Pattern](#42-timeout-pattern)
    - [4.3. Fallback Pattern](#43-fallback-pattern)

<!-- /TOC -->

# 1. Fault Tolerance System
Fault Tolerance는 시스템이 장애를 일으켜도 정상적으로 유지될 수 있도록 해준다. 한 상황을 예로 들어보자.
* 인터넷 전화 앱을 사용중에 스마트폰의 인터넷 연결이 끊겼다. Fault tolerance 시스템이 적용되지 않은 앱은 이 순간 멈춰버진다 (freezing). 작은 시스템 장애가 전체 시스템을 멈추게 만들었다.
* Fault tolerance 시스템을 적용한 앱은 인터넷이 끊기자 이를 해결하기 위한 과정에 들어간다. 인터넷이 다시 연결될때까지 일정한 주기로 서버에 데이터를 request를 한다. 몇 초 후에 인터넷이 돌아오고 앱은 다시 정상 작동한다.

fault tolerance 시스템은 작은 시스템 에러가 시스템의 total breakdown으로 이어지지 않도록 하는 "시스템 결함 방지" 시스템이며 예시가 보여주듯이 시스템을 디자인하는데에 있어 매우 중요한 요소라고 할 수 있겠다.

## 1.1. Digression -- Builder pattern
가끔 만든 class가 매우 다양한 instance 변수로 인해 highly configurable할 수 있다. 이런 경우에 각 변수의 값을 조정하는 constructor을 하나씩 만들게 되면 소스코드가 보기 안 좋고 길게 늘어지게 된다. 이 때 우리는 builder patter이라는 디자인 패턴을 통해서 좀 더 깔끔하게 필요한 변수는 설정을, 따로 설정이 필요하지 않은 변수에는 기본 값을 부여할 수 있다.

### 1.1.1. Builder Class
```java
public class User {
    private String name; // mandatory
    private String address; // optional
    private int age; //optional
    private String email; //optional
    private double location; //optional

    private User(UserBuilder builder) {
        name = builder.name;
        address = builder.address;
        age = builder.age;
        email = builder.email;
        location = builder.location;

    }

    public String toString() {
        return name + " " + address + " " + age + " " + email + " " + location;
    }

    public static class UserBuilder {
        private final String name;
        private int age;
        private String address;
        private String email;
        private double location;

        public UserBuilder(String s) {
            name = s;
            address = "none";
            age = -1;
            email = "none@none.com";
            location = 0.0;
        }

        public UserBuilder address(String a) {
            address = a;
            return this;
        }

        public UserBuilder age (int a) {
            age = a;
            return this;
        }

        public UserBuilder email (String e) {
            email = e;
            return this;
        }

        public UserBuilder location(double l) {
            location = l;
            return this;
        }

        public User build() {
            return new User(this);
        }
    }
}
```

### 1.1.2. Build User with builder class
```java
public class BuilderExample {

    public static void main(String args[]) {
        // Mint라는 유저를 만듬. 나머지 변수는 디폴드값.
        User user = new User.UserBuilder("Mint").build();
        System.out.println(user);

        // Rain라는 유저를 만듬. age, location 값을 조정함.
        User u = new User.UserBuilder("Rain")
            .age(19)
            .location(2.5)
            .build();
        System.out.println(u);

        // Sushi라는 유저를 만듬. address, email 값을 조정함.
        User u1 = new User.UserBuilder("sushi")
            .address("940 Tokyo")
            .email("sushu@yahoo.com")
            .build();
        System.out.println(u1);
    }
}
```

# 2. 시스템 에러의 종류
소프트웨어 시스템에서 일어날 수 있는 에러를 우리는 크게 2가지 타입으로 나누어서 볼 수 있다.

1. **Transient** - 가끔씩 한번 나오는 에러. 이에 대비해도 되지만 일어나도 시스템에 큰 피해를 입히지 않음.
2. **Persistent** - 자주 일어나는 에러. 시스템 어딘가에 오류가 있다는 징후. 빨리 해결하지 않으면 매우 심각한 시스템 장애로 번질 수 있음.

결론은 시스템에 발생하는 에러가 이 두개의 타입중에 어느쪽에 속하는지 빠르게 알아내어 이에 적절하게 반응할 수 있는 fault tolerance 시스템을 만드는것이 시스템 디자인에 궁극적인 목표라고 할 수 있겠다.

# 3. Fault Tolerance Design Pattern

## 3.1. Leaky Bucket Pattern
해석하면 "넘쳐흐르는 양동이 패턴"이 되겠다. 이 디자인 패턴은 현재 시스템에서 발생하는 에러가 transient 타입의 에러인지, persistent 타입의 에러인지 구분하게 해주며 이에 상응하는 조치를 취할 수 있도록 해준다.

* 이 패턴은 각각의 에러를 양동이안으로 떨어지는 물방울로 본다. 양동이 바닥에는 하나의 구멍이 뚫려 있어 안에 물이 일정 속도로 흘러내려간다 (밑 빠진 독에 물 붓기???). 양동이는 떨어지는 물방울들을 담을 수 있지만 더 많은 양의 물방울이 떨어질경우 어느정도 물이 차게 되면서 threshold을 지나 물이 흘러 넘치게 된다 (overflow).
* 이 관점에서 **물이 흘러 넘치기 시작하면 persistent 타입의 에러가 발생한 것**으로 간주한다. 너무 많은 양의 에러가 발생하고 있기 때문이다. 만약 물이 흘러 넘치지 않는다면 transient에러로 간주하고 소규모의 에러만 핸들링하면 될 것이다.

알고리즘을 설명해보면 이렇다.
1. 시스템에 에러가 도착한다.
2. 에러가 일어날때마다 Counter를 1씩 증가시킨다.
3. Counter가 미리 지정한 Threshold보다 클 경우 persistent 에러가 일어난것으로 간주한다.
4. 시스템 장애를 handling한다.
5. Counter는 일정 속도로 줄어든다 (leak).

비교적 간단한 시스템으로 네트워크 라우터등에서 사용되어진다고 한다.


# 4. Circuit Breaker Pattern
다음의 패턴은 "회로 차단기 패턴"이라고 해석 할 수 있겠다. 한 마디로 집에 전기 사용량이 비정상적일때 두꺼비 집이 내려가 집으로 들어오는 전력을 한번에 끊는 것처럼 이 패턴은 시스템에 지속되는 에러가 발생하였을때 대처하는 방법 중 하나이다.

* 현재 문제점은 불명의 에러가 지속적으로 발생하고 있으며 우리의 소프트웨어가 끔찍하게 당하고 있다.
* 사용할 회로 차단기는 이렇게 생겼다.
1. 3가지의 상태를 가진다. `열림`, `닫힘`, `반쯤 열림`
2. 처음에는 `닫힘` 상태에서 시작한다. 회로차단기는 성공 횟수 대비 에러 횟수를 지속적으로 기록한다.
3. 에러 횟수가 지정한 Threshold을 넘었을 경우 `열림` 상태로 전환한다. 열림 상태에서는 어떠한 메소드도 실행되지 않는다 (추가적인 에러를 방지하기 위해서).
4. 지정된 시간 (timeout period)가 지나면 `반쯤 열림` 상태로 전환한다. `반쯤 열린` 상태에서 test 메소드가 다시 실행된다. 만약 실패하면 다시 timout 시간 만큼 기다린뒤 재시도 한다. 성공 했을 경우, `닫힘` 상태로 돌아간다.

다음은 circuit breaker 패턴 사용의 예이다.

```java
CircuitBreakerPolicy breaker = new CircuitBreakerPolicyBuilder()
          .rateThreshold(90)  //rate of failure calls to trigger OPEN
          .sizeRingBufferHalfOpen(2) //size of test bucket
          .sizeRingBufferClosed(1) //size of the bucket           .build();
String result = (String) breaker.exec(service::doSomething);
```

## 4.1. Retry Pattern
다음의 패턴은 "재시도 패턴"이다. 말 그대로 에러가 발생했을 경우 재시도하는 방법이다. 성공할때 까지 계속해서 일정 시간 후에 재시도하는 노빠꾸 패턴이라고 보면 된다.

1. 에러가 발생 할 경우 일정 시간 기다린다.
2. 일정 시간 뒤에 재시도한다. 또 실패할 경우 다시 기다린다.

다음은 retry 패턴 사용의 예이다.
```java
RetryPolicy pol = new RetryPolicyBuilder()
    .attempts(5) //number of times to retry
    .waitDuration(1000) //Wait time between each try
    .build();
String result = (String) pol.exec(service::doSomething);
```

비교적 간단한 패턴이지만 의외로 쓸때가 많고 많은 경우 매우 효과적이다. 대표적으로 서버와의 통신에서 쓰인다.

## 4.2. Timeout Pattern
다음의 패턴은 "타임 아웃 패턴"이다. 이 패턴은 응답을 기다리고 있는 다른 서비스가 제시간안에 응답하지 않을 때 사용되는 패턴이다. 예로 에플리케이션이 서버에 응답을 기다리는데 응답하지 않을 경우 에플리케이션도 응답을 무기한 기다리며 함께 멈춰버릴 것이다 (hang). 이를 방지 하기 위한 패턴이다.

1. 서버에 응답을 요청한다.
2. 일정시간안에 서버가 응답을 하지 않는다면 더 이상 요청하지 않는다.

다음은 timeout 패턴 사용의 예이다.
```java
TimeoutPolicy pol = new TimeoutPolicyBuilder()
    .duration(500)
    .build();
String result = (String) pol.exec(service::doSomething);
```

## 4.3. Fallback Pattern
다음은 "뒤로 넘어지는 패턴(?)" 패턴이다. 말 그대로 뒤로 넘어지는게 아니라 메소드 A가 실패했을 경우 플랜 B에 해당하는 메소드 B가 실행되는 백업 패턴이다.

1. 메소드 A가 실행된다. 실패한다.
2. 메소드 B가 실행된다.

다음은 fallback 패턴 사용의 예이다.
```java
 FallbackPolicy pol = new FallbackPolicyBuilder(service::doBackupFunction)
    .build();
String result = (String) pol.exec(service::doSomething);
```




