# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. Queues](#2-queues)
    - [2.1. Characteristics](#21-characteristics)
    - [2.2. Operations](#22-operations)
- [3. Efficiencies](#3-efficiencies)
    - [3.1. Time Compleixty compare to other data strucures](#31-time-compleixty-compare-to-other-data-strucures)

<!-- /TOC -->

# 2. Queues
## 2.1. Characteristics
* Abstract data type (multiple implementations with different backing data structures)
* First In, First Out (`FIFO`)
* Can not access element except on the top of the queue
* Linear data strucutres are used for implementation (array, linkedList)

## 2.2. Operations
* `void enqueue(x)`
* `x dequeue()`
* `x peek()`
* `int size()`
* `boolean isEmpty()`

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
