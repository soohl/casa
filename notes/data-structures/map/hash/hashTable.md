# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. HashMap](#2-hashmap)
    - [2.1. HashMap vs HashTable](#21-hashmap-vs-hashtable)
    - [2.2. Operations (HashMap ADT)](#22-operations-hashmap-adt)
- [3. Efficiencies](#3-efficiencies)
    - [3.1. Time Complexity](#31-time-complexity)
    - [3.2. Space Complexity](#32-space-complexity)

<!-- /TOC -->
# 2. HashMap

## 2.1. HashMap vs HashTable
HashMap | HashTable
|---|---|
Asynchronous|Synchronous
Simple|Complex
Fast, less space|Slow, more space
Allows null keys/values|Does not allow null keys or values
Iterator to see all values|Enumerator to see all values
* `Async` - do task before other finishes
* `Sync` - wait until one task finishes, and to other

## 2.2. Operations (HashMap ADT)
* `v put(<k,v>)` - takes in an entry and puts it in the HashMap
* `v get(k)` - takes in a keym returns the value associated with it
* `<k,v> remove(k)` - takes in key, removes and returns the entry with that key
* `int size()` - returns the size

# 3. Efficiencies

## 3.1. Time Complexity
|Operation|Best Case | Worst Case | Average Case|
|---|---|---|---|
|search|`O(1)`|`O(n)`|`O(1)`|
|add|`O(1)`|`O(n)`|`O(1)`|
|remove|`O(1)`|`O(n)`|`O(1)`|

## 3.2. Space Complexity
Always `O(n)`