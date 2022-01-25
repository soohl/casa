
# 1. Singleton Pattern
<!-- TOC -->

- [1. Singleton Pattern](#1-singleton-pattern)
    - [1.1. Definition](#11-definition)
    - [1.2. Concept](#12-concept)
    - [1.3. When we use Singleton pattern?](#13-when-we-use-singleton-pattern)
    - [1.4. Real-World Example](#14-real-world-example)
    - [1.5. Computer-World Example](#15-computer-world-example)
    - [1.6. Lazy Initialization Implementation](#16-lazy-initialization-implementation)
        - [1.6.1. Characteristics](#161-characteristics)
        - [1.6.2. Why making the class final?](#162-why-making-the-class-final)
    - [1.7. Eager Initialization Implementation](#17-eager-initialization-implementation)
        - [1.7.1. Characteristics](#171-characteristics)
        - [1.7.2. Pros and Cons](#172-pros-and-cons)
    - [1.8. Bill Pugh's Implementation](#18-bill-pughs-implementation)
        - [1.8.1. Characteristics](#181-characteristics)
    - [1.9. Double-Checked Locking](#19-double-checked-locking)
        - [1.9.1. Characteristics](#191-characteristics)

<!-- /TOC -->

## 1.1. Definition
Singleton pattern ensure a class only has one instance, and provide global point of access to it. 

## 1.2. Concept
A class cannot have multiple instances. Once created, the next time onward, you use only the existing instance. This approach helps you restrict unnecessary object creations in a centralized system. The approach also promotes easy maintenance. 

## 1.3. When we use Singleton pattern?
In general, you can use singleton pattern to implement a centralized management system, to maintain common log file, to maintain thread pools in a multithreaded environment, to implement caching mechanism or device drivers, and so forth. 

## 1.4. Real-World Example
1. You are a member of a sports team, and the team is participating in a tournament.
2. The captain of each team has to do a coin flip before every game starts. 
3. You do not have to repeat the process of nominating a captain from your team, if you already have done so. 
4. From every team member's persepctive, there should be only one captain of the team. 

## 1.5. Computer-World Example
In some specific software systems, you may prefer to use only one file system for centralized management of resources. Also, singleton pattern can implement a caching mechanism. 

## 1.6. Lazy Initialization Implementation
* The constructor is private to prevent the use of a "new" operator.
* Simply reuse the existing instance of the class. If not, create new one. 
```java
final class Captain
{
    private static Captain captain; 

    private Captain() {     }

    // Make sure multiple instance is not created from different thread. 
    public static synchronized Captain getCaptain()
    {
        // Lazy initialization
        if (captain == null) {
            captain = new Captain();
            System.out.println("New captain is elected from your team");
        } else {
            System.out.println("We already have a captain");
            System.out.println("Send him for the tose");
        }
        return captain;
    } 
}
```

```java
public class SingletonPatternExample {
    public static void main(String[] args) {
        System.out.println("Singleton Demo");
        // Captain c = new Captain(); Error since the constructor is a private
        Captain C1 = Captain.getCaptain();
        Captain C2 = Captain.getCaptain();
        if (C1 == C2) {
            System.out.println("C1 and C2 are same instances");
        }
    }
}
```
### 1.6.1. Characteristics

* Since the constructor is private, we can not instantiate the Singleton class outside. It helps us to refer the only instance that can exist in the system, and at the same time, we restrict the additional object creation of the Captain class.
* The private constructor also ensures that the Captain class cannot be extended. So, subclasses cannot misuse the concept. 
* Used "`synchronized`" keyword, so mlultiple thread cannot involve in the instantiation process at the same time. It is forcing each thread to wait its turn to get the method, so thread-safety is ensured. But **synchronization is costly operation**, and one the instance is created, it is additional inefficiency. 
* **Lazy initialization** is a technique which we delay the object creation process. In this implementation, the object is not created until the first `getCaptain()` method call. 

### 1.6.2. Why making the class final? 
Since the constructor is in `private`, we can prevent our subclasses from creating a new instances. However, in case of using nested class, using `final` class is better practice. 

```java
//final class Captain
class Captain
{
    private static Captain captain; 
    static int numOfInstances = 0;
    private Captain() {
        numOfInstances++;
        System.out.println("Number of instances of Captain: " + numOfInstances);
    }

    // Make sure multiple instance is not created from different thread. 
    public static synchronized Captain getCaptain()
    {
        // Lazy initialization
        if (captain == null) {
            captain = new Captain();
            System.out.println("New captain is elected from your team");
        } else {
            System.out.println("We already have a captain");
            System.out.println("Send him for the tose");
        }
        return captain;
    }
    // A non-static nested class (inner class) 
    public class CaptainDerived extends Captain {
        // Some Code
    }
}
```

```java
public class SingletonPatternExample {
    public static void main(String[] args) {
        System.out.println("Singleton Demo");
        // Captain c = new Captain(); Error since the constructor is a private
        Captain C1 = Captain.getCaptain();
        Captain C2 = Captain.getCaptain();
        if (C1 == C2) {
            System.out.println("C1 and C2 are same instances");
        }
        Captain.CaptainDerived derived = C1.new CaptainDerived();
    }
}
// OUTPUT: Number of instances of Captain: 2
```
In this case, two instances are created, which violates Singleton pattern's objective. Thus, it is important practice to make the class `final`.

## 1.7. Eager Initialization Implementation

```java
class Captain {

    //Early initilization
    private static final captain = new Captain();
    // Private constructor to prevent further instantiation
    private Captain() {
        System.out.println("A captain is elected");
    }
    // Public access to the single instance. 
    public static Captain getCaptain() {
        System.out.println("Here is our captain");
        return captain;
    }
    // 
    public static void dummayMethod() {
        System.out.println("This is a dummy method");
    }
}
```
### 1.7.1. Characteristics
* Different from lazy initialization approach, since the one and only instance is created at the very beginning, even before `getCaptain()` method is called.
* Not a very good practice.

### 1.7.2. Pros and Cons
**Pros**
* It is straightforward and cleaner
* It is opposite of lazy initialization, but still thread safe. 
* It has small lag time when the application is in execution mode because everything (isntance) has already been loaded in the memory. 

**Cons**
* The application takes longer time to start (compared to lazy initialization) becuase everything is loaded first.

## 1.8. Bill Pugh's Implementation
```java
class Captain {

    private Captain() {
        System.out.println("A captain is elected");
    }

    // Special helper class
    private static class SingletonHelper {
        // Nested class is referenced after getCaptain() is called. 
        private static final Captain captain = new Captain();
    }

    public static Captain getCaptain() {
        return SingletonHelper.captain;
    }

    public static void dummyMethod() {
        System.out.println("This is a dummy method");
    }
}
```
### 1.8.1. Characteristics
* Do not use a synchronization techinique nor eager initialization. 
* SingletonHelper is considered only when `getCaptain()` is called. 
* *Dummy method will not produce output* until SingletonHelper class is referenced. This is different from eager implementation
* One of the common and standard methods for implementing Singleton in Java. 

## 1.9. Double-Checked Locking
```java
final class Captain {

    private static Captain captain;
    static int numOfInstances = 0;

    private Captain() {
        numOfInstances++;
        System.out.println("Number of instances of Captain: " + numOfInstances);
    }

    public static Captain getCaptain() {
        if (captain == null) {
            synchronized (Captain.class) {
                // Lazy Initialization
                if (captain == null) {
                    captain = new Captain();
                    System.out.println("New captain is elected");
                } else {
                    System.out.println("We already have captain");
                    System.out.println("Send him for the toss");
                }
            }
        }
        return captain;
    }
}
// Output = numOfInstances = 1
```
### 1.9.1. Characteristics
* Uses `if` statement to make sure the first object creation is `synchronized` for thread safety, but not after the creation to increase the thread utilization. 
* `synchronized` inside the `if` statement
* More effecient use of threads than early implementations
* One the popular option

