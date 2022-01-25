# 1. Flyweight Pattern
<!-- TOC -->

- [1. Flyweight Pattern](#1-flyweight-pattern)
    - [1.1. Definition](#11-definition)
    - [1.2. Concept](#12-concept)
    - [1.3. Real-World Example](#13-real-world-example)
    - [1.4. Computer-World Example](#14-computer-world-example)
    - [1.5. Implementation](#15-implementation)
    - [1.6. Characteristics](#16-characteristics)
    - [1.7. Advantage of flyweight patern](#17-advantage-of-flyweight-patern)
    - [1.8. Challenges with flyweight pattern](#18-challenges-with-flyweight-pattern)

<!-- /TOC -->
## 1.1. Definition
Use sharing to support large numbers of fine-grained objects efficiently

## 1.2. Concept 
> A flyweight is a shared object that can be used in multiple contexts simultaneously. The flyweight acts as an independent object in each context - it's indeistinguishable from an instance of the object that's not shared. Flyweights cannot make assumptions about the context in which they operate. (Addison-Wesley, 1955)

* Pattern is useful when you need a large number of similar objects that are unique in terms of only a few parameters and most of the stuffs are common in general. 
* A flyweight is an object. It tries to minimize memory usage by sharing data as much as possible with other similar objects. Sharing objects may allow their usage at fine granularities with minimum costs. 
* Two common terms are used in this context: **extrinsic** and **intrinsic**. 

**Intrinsic**
* An intrinsic state is stored/shared in the flyweight's object, and it is independent of flyweight's context. 
* Experts suggest that while implementing this pattern, we should make intrinsic states immutable. 

**Extrinsic**
* An extrinsic state varies with flyweight's context, which is why they cannot be shared. Client objects maintain the extrinsic state, and they need to pass this into a flyweight. 
* If required, clients can also compute the extrinisic state on the fly when using flyweights. 

## 1.3. Real-World Example
Suppose that you have pen. You can replace different refills to write with different colors. So, a pen without refills is considered as a flyweight with instrinsic data, and a pen with refills is considered as extrinsic data.

Supposed the company needs to print visiting cards for its employees. The company can create a common template with the company logo, address etc (intrinsic), and later add each employee's contact information (extrinsic) on the cards. 

## 1.4. Computer-World Example
You want to create a website where user can compile and excute various programming language (Java,CPP,Python etc). It will take too much time for server set up a unique environment for every different language. Instead, we can make a common programming environment (that supports various lanaguage) and later make decisions whether we need to create a new one, or maintain the factory.

You want to create a computer game, where large number of participants have same core structures but different appearances (colors, weapone etc). Instead of creating and storing all of these objects with different variations, we can design the system such that we create these instances with common properties (flyweights and intrinsic) and the client object maintains all of these variations (extrinsic state). 

Graphical representation in word processor also utilizes flyweight pattern. 

## 1.5. Implementation

```java
interface Robot
{
    //Color comes from client.It is extrinsic.
    void showMe(String color);
}
```

```java
//A shared flyweight implementation
class SmallRobot implements Robot
{
    /*
     * Intrinsic state.
     * It is not supplied by client.
     * So, it is independent of the flyweight’s context.
     * This can be shared across.
     * These data are often immutable.
     */
    private final String robotTypeCreated;
    public SmallRobot()
    {
           robotTypeCreated="A small robot created";
           System.out.print(robotTypeCreated);
    }
    @Override
    public void showMe(String color)
    {
        System.out.print(" with " +color + " color");
    }
}
```

```java
//A shared flyweight implementation
class LargeRobot implements Robot
{
    /*
     * Intrinsic state.
     * It is not supplied by client .
     * So, it is independent of the flyweight’s context.
     * This can be shared across.
     * These data are often immutable.
     */
    private final String robotTypeCreated;
    public LargeRobot()
    {
        robotTypeCreated="A large robot created";
        System.out.print(robotTypeCreated);
    }
    @Override
    public void showMe(String color)
    {
        System.out.print(" with " + color + " color");
    }
}
```

```java
//An unshared flyweight implementation
class FixedSizeRobot implements Robot
{
    /*
     * Intrinsic state.
     * It is not supplied by client.
     * So, it is independent of the flyweight’s context.
     * This can be shared acorss.
     */
    private final String robotTypeCreated;
    public FixedSizeRobot()
    {
        robotTypeCreated="A robot with a fixed size created";
        System.out.print(robotTypeCreated);
    }
    @Override
    //Ingoring the extrinsic state argument
    //Since it is an unshared flyweight
    public void showMe(String color)
    {
        System.out.print(" with " + " blue (default) color");
    }
}
```

```java
import java.util.Map;
import java.util.HashMap;
import java.util.Random;

class RobotFactory
{
    static Map<String, Robot> robotFactory = new HashMap<String, Robot>();
    public int totalObjectsCreated()
    {
        return robotFactory.size();
    }
    public static synchronized Robot getRobotFromFactory(String robotType) throws Exception
    {
        Robot robotCategory = robotFactory.get(robotType);
        if(robotCategory==null)
        {
            switch (robotType)
            {
            case "small":
                System.out.println("We do not have Small Robot at present.So we are creating a small robot now.") ;
                robotCategory = new SmallRobot();
                break;
            case "large":
                System.out.println("We do not have Large Robot at present.So we are creating a large robot now.");
                robotCategory = new LargeRobot();
                break;
            case "fixed":
                System.out.println("We do not have fixed size at present. So we are creating a fixed size robot now.");
                robotCategory = new FixedSizeRobot();
                break;
            default:
                throw new Exception(" Robot Factory can create only small ,large or fixed size robots");
            }
            robotFactory.put(robotType,robotCategory);
        }
        else
        {
            System.out.print("\n \t Using existing "+ robotType +" robot and coloring it" );
        }
        return robotCategory;
    }
}
```

```java
import java.util.Random;

public class FlyweightPatternExample {
    public static void main(String[] args) throws Exception {
        RobotFactory robotFactory = new RobotFactory();
        System.out.println("\n***Flyweight Pattern Example ***\n");
        Robot myRobot;

        //Here we are trying to get 3 Small type robots
        for (int i = 0; i < 3; i++)
        {
            myRobot = RobotFactory.getRobotFromFactory("small");
            /*
            Not required to add sleep().But it is included to
            increase the probability of getting a new random number
            to see the variations in the output .
             */
            Thread.sleep(1000);
            //The extrinsic property color is supplied by the client code.
            myRobot.showMe(getRandomColor());
        }
        int numOfDistinctRobots = robotFactory.totalObjectsCreated();
        System.out.println("\n Till now, total no of distinct robot objects created: " + numOfDistinctRobots);
        //Here we are trying to get 5 Large type robots
        for (int i = 0; i < 5; i++)
        {
            myRobot = RobotFactory.getRobotFromFactory("large");
            /*
            Not required to add sleep().But it is included to
            increase the probability of getting a new random number
            to see the variations in the output.
             */
            Thread.sleep(1000);
            //The extrinsic property color is supplied by the client code.
            myRobot.showMe(getRandomColor());
        }
        numOfDistinctRobots = robotFactory.totalObjectsCreated();
        System.out.println("\n Till now, total no of distinct robot objects created: " + numOfDistinctRobots);
        //Here we are trying to get 4 fixed sizerobots
        for (int i = 0; i < 4; i++)
        {
            myRobot = RobotFactory.getRobotFromFactory("fixed");
            /*
            Not required to add sleep().But it is included to
            increase the probability of getting a new random number
            to see the variations in the output.
             */
            Thread.sleep(1000);
            //The extrinsic property color is supplied by the client code.
            myRobot.showMe(getRandomColor());
        }
        numOfDistinctRobots = robotFactory.totalObjectsCreated();
        System.out.println("\n Till now, total no of distinct robot objects created: " + numOfDistinctRobots);
    }
    static String getRandomColor()
    {
        Random r = new Random();
        /* I am simply checking the random number generated that can be either an even number or an odd number. And based on that we are choosing the color. For simplicity, I am using only two colors-red and green
         */
        int random = r.nextInt();
        if (random % 2 == 0)
        {
            return "red";
        }
        else
        {
            return "green";
        }
    }
}
```
## 1.6. Characteristics 
* The cliend needed to create 12 robots (3 small, 5 large, 4 fixed size) but these demand are served by only 3 distinct template objects and these were configured on the fly. 
* Fixed-size robot never changed since it ignored to represent an unshared flyweight.

## 1.7. Advantage of flyweight patern
* Can reduce memory consumption of heavy objects
* Can reduce the total number of "similar" objects in the system
* Can provide centralized mechanism to control the states of many "virtual" objects. 

## 1.8. Challenges with flyweight pattern
* Takes time to configure flyweights
* Require additional layer of abstraction of the common template, that makes it hard to debug and maintain. 
* Logical instances of a class cannot behave differently from other instances. 
* Often used with singleton pattern for protecting singularity, which often cost performance.  




