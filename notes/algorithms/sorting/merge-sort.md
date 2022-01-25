<!-- TOC -->

- [1. Properties](#1-properties)
- [2. Operations](#2-operations)
- [3. Efficiencies](#3-efficiencies)

<!-- /TOC -->
# 1. Properties
* Stable
* Not Adaptive
* Out-of-place

# 2. Operations
1. Divide array by two equal parts. (right, left)
2. Perform merge sort on each half. 
3. Merge two parts together.

# 3. Efficiencies
|Case|Big O|When|
|---|---|---|
|Best|`O(nlog(n))`|array is perfectly sorted, but still have to go over `nlog(n)` for merge sort|
|Worst|`O(nlog(n))`|array is perfectly un-sorted|
|Average|`O(nlog(n))`||