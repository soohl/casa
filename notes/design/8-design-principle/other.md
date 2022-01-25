<!-- TOC -->

- [1. Other Design Principles](#1-other-design-principles)
- [2. Law of Demeter](#2-law-of-demeter)
- [3. Tell, Don't Ask](#3-tell-dont-ask)
- [4. Command Query Segregation](#4-command-query-segregation)

<!-- /TOC -->

# 1. Other Design Principles

# 2. Law of Demeter
**An Object only sends messages to:**
* Itself (its own instance methods)
* Objects sent as arguments to message m
* Objects created as part of reaction to m
* Objects directly accessible via my attributes

Purpose: **Reduce coupling**, fragility, rigid

*Example)*
**Not a good design**
```java
/// Server class method ///
send2User(User u) {
    um.getUser(u).getConnection().getSocket().send(msj);
}
* Violation of law of demeter since you can not call along classes chaining.
```

**Correction**
* Create `send(user,msj)` in userManager
* Server class does not need to traverse over the classes.
```java
/// Server class method ///
send2User(User u) {
    um.send(u,msj);
}
```

# 3. Tell, Don't Ask
* Tell objects what to do, do not ask them about internal state and then make decisions. 
* Isolate business logic to appropriate class.
* DRY

# 4. Command Query Segregation
* **Query** – asking for information, should not do any processing
* **Command** – asking for processing, should not return information

*This is a somewhat controversial one – apply where it makes sense*


