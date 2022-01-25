# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. Singly Linked Lists](#2-singly-linked-lists)
    - [2.1. Characteristics](#21-characteristics)
        - [2.1.1. Extension](#211-extension)
    - [2.2. Operations](#22-operations)
- [3. Efficiencies](#3-efficiencies)
    - [3.1. Time Complexity](#31-time-complexity)

<!-- /TOC -->

# 2. Singly Linked Lists

## 2.1. Characteristics

```
|------------------|
|  Data  | Address |----->
|------------------|
```

* Consists node (data + address)
* Head reference to track the list
* If the list is empty, the head is null

### 2.1.1. Extension
* Keep a size variable
* Create a tail reference
* Use generic

## 2.2. Operations
* `addToFront()` - `O(1)`
1. Create new node
2. Point the new node's next to the head
3. Set the new node to be the head
* `addToBack()` - `O(n)`
1. Iterate until current's next is null, not until current is null
2. Edge case -> if the head is null, point the head to the new node
* `removeFromFront()`
1. Save the data from the head for returning
2. Set head equal to head's next
* `removeFromBack()`
1. Set current equal to head
2. Loop until current's next next is null.
3. Edge case ->size is 0 or 1

# 3. Efficiencies
## 3.1. Time Complexity
|Operation|Best Case | Worst Case | Average Case|
|---|---|---|---|
|search|`O(1)`|`O(n)`|`O(n)`|
|add front|`O(1)`|`O(1)`|`O(1)`|
|add back|`O(1)`|`O(n)`|`O(n)`|
|remove front|`O(1)`|`O(1)`|`O(1)`|
|remove back|`O(1)`|`O(n)`|`O(n)`|