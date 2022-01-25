<!-- TOC -->

- [1. Basic Principles (SOLID)](#1-basic-principles-solid)
    - [1.1. Single Responsibility](#11-single-responsibility)
    - [1.2. Open / Closed](#12-open--closed)
    - [1.3. Liskov Substitution Property](#13-liskov-substitution-property)
    - [1.4. Interface Segregation Principle](#14-interface-segregation-principle)
    - [1.5. Dependency Inversion Principle (Dependency Injection)](#15-dependency-inversion-principle-dependency-injection)

<!-- /TOC -->

# 1. Basic Principles (SOLID)

* S = Single Responsibility
* O = Open / Closed
* L = Liskov Substitution
* I - Interface Segreagation
* D = Dependency Inversion

## 1.1. Single Responsibility
* Each class should have a single overriding responsibility (High Cohesion)
* Each class has one reason why it should change

## 1.2. Open / Closed
* Objects are open for **extension** but closed for **modification**.
* Extension via inheritance, polymorphism.

## 1.3. Liskov Substitution Property
> If for each object `o1` of type `S` there is an object `o2 `of type `T` such that for all programs `P` defined in terms of `T`, the behavior of `P` is unchanged when `o1` is substituted for `o2`, then `S` is a subtype of `T`. [Liskov88]

* Subclasses should be substitutable for their base classes.

*Example)*
```java
Squre, Rectangle problem
validate(Retangle r) {
    r.setLength(5);
    r.setWidth(6); 
}
* Valid() not work when square is passed. 
* Use of (r instance of square) {l, w are 6} violates law
```

**Contract Implications**
* Preconditions cannot be strengthened in the subclass
* Postconditions cannot be weakened in the subclass
* If your function refers to a base class, but has to know the specific subclass then it probably violates this principle

## 1.4. Interface Segregation Principle
* Don’t make large multipurpose interfaces – instead use several small focused ones.
* Don’t make clients depend on interfaces they don’t use.
* Class should depend on each other through the smallest possible interface.

## 1.5. Dependency Inversion Principle (Dependency Injection)
* Use interface as frequently as possible
* Depends on abstraction not concrete class


