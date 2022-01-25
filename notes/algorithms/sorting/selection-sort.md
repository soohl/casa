<!-- TOC -->

- [1. Properties](#1-properties)
- [2. Operations](#2-operations)
- [3. Efficiencies](#3-efficiencies)

<!-- /TOC -->
# 1. Properties
* Unstable
* Not Adaptable
* In-place

# 2. Operations
1. Iterate from `1st` to `n` element and find maximum element
2. Swap max element with `n`
3. Repeat 1-2 but swap with `n-i` element, where `i++`.
4. Every iteration guarentee one more sorted element at the end. 

# 3. Efficiencies
|Case|Big O|When|
|---|---|---|
|Best|`O(n^2)`|array is already sorted, but still has to go over `n(n-1)/2` time. (no early termination)|
|Worst|`O(n^2)`||
|Average|`O(n^2)`||

Altough it has `O(n^2)`, it minimizes the swaps, so use when memory writing operation is very expensive. 
