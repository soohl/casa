# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. ArrayList](#2-arraylist)
    - [2.1. Characteristics](#21-characteristics)
    - [2.2. Pros](#22-pros)
    - [2.3. Cons](#23-cons)
    - [2.4. Operations](#24-operations)
- [3. Efficiencies](#3-efficiencies)
    - [3.1. Time Complexity](#31-time-complexity)

<!-- /TOC -->
# 2. ArrayList

## 2.1. Characteristics
* Dyanamic
* Contigeous memory
* No null space between elements

## 2.2. Pros
* Dynamic data type (flexible storage size)
* Easy operations (does not have to know the index)

## 2.3. Cons
* Can not store primitives (only objective) - need wrapper
* Still `O(n)` when resizing as it is backed by array

## 2.4. Operations
* Add to front - `O(n)`
* Add to back - `amortized O(1)`; due to `O(n)` resize operation if needed.
* Add to index - `O(n)`
* Remove from front - `O(n)`; due to shifting elements
* Remove from back - `O(1)`
* Access specific index - `O(1)`

# 3. Efficiencies
## 3.1. Time Complexity
|Operation|Best Case | Worst Case | Average Case|
|---|---|---|---|
|access|`O(1)`|`O(1)`|`O(1)`|
|search|`O(1)`|`O(n)`|`O(n)`|
|add front|`O(1)`|`O(n)`|`O(n)`|
|add back|`O(1)`|`O(n)`|`amortized O(1)`|
|remove front|`O(1)`|`O(n)`|`O(n)`|
|remove back|`O(1)`|`O(1)`|`O(1)`|