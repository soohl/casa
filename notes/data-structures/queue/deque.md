# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. Double-ended Queue (DEQUE)](#2-double-ended-queue-deque)
    - [2.1. Characteristics](#21-characteristics)
    - [2.2. Operations](#22-operations)
- [3. Efficiencies](#3-efficiencies)
    - [3.1. Time Compleixty compare to other data strucures](#31-time-compleixty-compare-to-other-data-strucures)

<!-- /TOC -->

# 2. Double-ended Queue (DEQUE)
## 2.1. Characteristics
* Abstract data type (multiple implementations with different backing data structures)
* Does not have a `LIFO` or `FIFO` behavior
* Can perform add/remove operations from both ends of the structure

## 2.2. Operations
* `addFirst(x)`
* `addLast(x)`
* `x removeFirst()`
* `x removeLast()`

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