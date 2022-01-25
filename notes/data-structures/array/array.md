# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. Array](#2-array)
    - [2.1. Characteristics](#21-characteristics)
    - [2.2. Pros](#22-pros)
    - [2.3. Cons](#23-cons)
- [3. Efficiency](#3-efficiency)
    - [3.1. Time Complexity](#31-time-complexity)

<!-- /TOC -->
# 2. Array

## 2.1. Characteristics
* Static
* Contigeous memory

## 2.2. Pros
* Flexible storage type (object, primitive, references...)
* Constant time when index is known (searching : `O(n)`)

## 2.3. Cons
* Time complexity of `O(n)` if the size of the arrray must be doubled
* Space complexity of `O(2n)` if the size of the arrray must be doubled
* Takes constant memory space (may not be efficient in some case)

# 3. Efficiency

## 3.1. Time Complexity
|Operation|Best Case | Worst Case | Average Case|
|---|---|---|---|
|access|`O(1)`|`O(1)`|`O(1)`|
|add|`O(n)`|`O(n)`|`O(n)`|
|search|`O(1)`|`O(n)`|`O(n)`|
|remove|`O(1)`|`O(n)`|`O(n)`|