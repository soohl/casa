# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. Circularly Singly Linked Lists](#2-circularly-singly-linked-lists)
    - [2.1. Characteristics:](#21-characteristics)
    - [2.2. Operations: (with head reference only)](#22-operations-with-head-reference-only)
- [3. Efficiencies](#3-efficiencies)
    - [3.1. Time Complexity](#31-time-complexity)

<!-- /TOC -->


# 2. Circularly Singly Linked Lists

## 2.1. Characteristics:
```
|------------------|      |------------------|
|  Data  | Address |----->|  Data  | Address |--|
|------------------|      |------------------|  |
         |                                      |
         |---------------------------------------
```
* The last node in the list points back to the head
* Can no longer use `current == null` to cehck the end
* Use `current == head` instead

## 2.2. Operations: (with head reference only)

* `addToFront()` - `O(1)`
1. Crete new empty node
2. Connect the node to the list (set the new node's next to head's next)
3. Connect the list to the node (set head's next to the new node)
4. Put the data from the head into the new node (copy data)
5. Put the data we want to add into the head node

* `addToBack()` - `O(1)`
1. Perform addToFron()
2. Move the head to head's next

* `removeFromFront()` - `O(1)`
1. Save the data from the head to return it later
2. Copy the data from head's next into the head
3. Set head's next pointer to head's next next.

* `removeFromBack()` - `O(n)`
1. Iterate to the last last node (next next current == null)
2. Connect to the head

# 3. Efficiencies
## 3.1. Time Complexity
|Operation|Best Case | Worst Case | Average Case|
|---|---|---|---|
|search|`O(1)`|`O(n)`|`O(n)`|
|add front|`O(1)`|`O(1)`|`O(1)`|
|add back|`O(1)`|`O(1)`|`O(1)`|
|remove front|`O(1)`|`O(1)`|`O(1)`|
|remove back|`O(1)`|`O(n)`|`O(n)`|