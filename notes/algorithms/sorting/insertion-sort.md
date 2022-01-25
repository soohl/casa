<!-- TOC -->

- [1. Properties](#1-properties)
- [2. Operations](#2-operations)
- [3. Efficiencies](#3-efficiencies)

<!-- /TOC -->
# 1. Properties
* Stable
* Adaptable
* In-place

# 2. Operations
1. Swap first element and second element if out-of-order. 
2. Continue this process to `n`. 
3. For each iteration, check if all the previous element is sorted. 

# 3. Efficiencies
|Case|Big O|When|
|---|---|---|
|Best|`O(n)`|array is already sorted, but still has to go over `n` element once.|
|Worst|`O(n^2)`|array is perfectly un-sorted, so we need to go over `n(n-1)/2` operations.|
|Average|`O(n^2)`||