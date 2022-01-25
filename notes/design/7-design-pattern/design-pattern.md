<!-- TOC -->

- [1. Design pattern](#1-design-pattern)
    - [1.1. Singleton Pattern](#11-singleton-pattern)
    - [1.2. Builder Pattern](#12-builder-pattern)
    - [1.3. Flyweight Pattern](#13-flyweight-pattern)

<!-- /TOC -->

# 1. Design pattern

## 1.1. Singleton Pattern
Singleton pattern is a software design pattern that restricts the instantiation of a class to one.

* Ensure that only one instance of the singleton class ever exists
* Provide global access to that instance

```java
* Declare all constructors of the class to private
* Provide static method that returns the instance

public final class Singleton {

    private static final Singleton INSTANCE = new Singleton();

    private Singleton() {}

    public static Singleton getInstance() {
        return INSTANCE;
    }
}
```

## 1.2. Builder Pattern
Refer to fault tolerance document.

## 1.3. Flyweight Pattern
Flyweight pattern is primarily used to reduce the number of objects created and to decrease memory footprint and increase performance. This type of design pattern comes under structural pattern as this pattern provides ways to decrease object count thus improving the object structure of application.


* Share attributes that are same 
* Based on a factory which recycles created objects by storing them after creation. Each time an object is requested, the factory looks up the object in order to check if it’s already been created. If it has, the existing object is returned – otherwise, a new one is created, stored and then returned.

```
* Share attributes that are same (may use interface)
        Type
|----------------->
ship          shipType
- fuel        - maxFuel
- cargo       - maxDam
- damage      - maxCargo
```
> https://www.tutorialspoint.com/design_pattern/flyweight_pattern.htm