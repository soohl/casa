# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. Doubly Linked Lists](#2-doubly-linked-lists)
    - [2.1. Characteristics](#21-characteristics)
    - [2.2. Operations](#22-operations)
- [3. Efficiencies](#3-efficiencies)
    - [3.1. Time Complexity](#31-time-complexity)

<!-- /TOC -->

# 2. Doubly Linked Lists

## 2.1. Characteristics
```
      |--------------------------|
<-----|  Prev |  Data  | Address |----->
      |--------------------------|
```
* Two pointer each pointing to the previous node and the next node
* Always have both a **head** and **tail** pointer
* At size = 0, both the head and the tail is null
* At size = 1, both the head and the tail to the single node

## 2.2. Operations
* `addToFront()` - `O(1)`
1. Create new node
2. Connect the new node to the list (set new node's next to the head)
3. Connect the list to the new node (set head's previous to the new node)
4. Point the head to the new node

* `addToBack()` - `O(1)`
1. Create new node
2. Connect the node to the list (set the new node's prev. to the tail)
3. Connect the list to the node (set the tail's next to the new node)
4. Point the tail to the new node

* `removeFromFront()`
1. Set the head to head's next
2. Set the head's prev. to null

* `removeFromBack()`
1. Set the head to head's next
2. Set the head's prev. to null

*Edge case:* remove the list with size = 1
* Set head and tail to null

**Always change the head/tail after everything else has been connected. It may result in lose of reference point.**

# 3. Efficiencies
## 3.1. Time Complexity
|Operation|Best Case | Worst Case | Average Case|
|---|---|---|---|
|search|`O(1)`|`O(n)`|`O(n)`|
|add front|`O(1)`|`O(1)`|`O(1)`|
|add back|`O(1)`|`O(1)`|`O(1)`|
|remove front|`O(1)`|`O(1)`|`O(1)`|
|remove back|`O(1)`|`O(1)`|`O(1)`|