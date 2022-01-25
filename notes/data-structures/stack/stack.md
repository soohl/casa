# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. Stacks](#2-stacks)
    - [2.1. Characteristics:](#21-characteristics)
    - [2.2. Operations:](#22-operations)
- [3. Efficiencies](#3-efficiencies)
    - [3.1. Time Compleixty compare to other data strucures](#31-time-compleixty-compare-to-other-data-strucures)

<!-- /TOC -->

# 2. Stacks
## 2.1. Characteristics:
* Abstract data type (multiple implementations with different backing data structures)
* Last In, First Out (`LIFO`)
* Can not access element except on the top of the stack
* Linear data strucutres are used for implementation (array, linkedList)

## 2.2. Operations:
* `void push(x)`
* `x pop()`
* `x top()/peek()`
* `int size()`
* `boolean isEmpty()`
* `void clear()`

# 3. Efficiencies
## 3.1. Time Compleixty compare to other data strucures
|Complexity|Access|Search|Add(to front)|Remove (from front)|
----|----|----|----|----
| Array |`O(1)`|`O(n)`|`O(n)`|`O(n)`|
| SLL |`O(n)`|`O(n`)|`O(1)`|`O(1)`|
| DLL |`O(n)`|`O(n)`|`O(1)`|`O(1)`|
| Stack |`O(n)`|`O(n)`|`O(1)`|`O(1)`|
| Queue |`O(n)`|`O(n)`|`O(1)`|`O(1)`|
| Deque |`O(n)`|`O(n)`|`O(1)`|`O(1)`|
