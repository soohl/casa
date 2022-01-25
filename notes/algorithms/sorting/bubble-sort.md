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
1. From the first element, compare with the next element and swap if it is out of order (either ascending or descending). 
2. Repeat Until the end.
3. Last element is guarenteed to be biggest (for ascending)
4. Repeat 1-3 without comparing with the last X elements (X increment by 1 for each iteration)
5. When nothing is swapped, array is already sorted, so stop sorting.

# 3. Efficiencies

|Case|Big O|When|
|---|---|---|
|Best|`O(n)`|array is already sorted, but still has to go over `n` element once.|
|Worst|`O(n^2)`|array is perfectly un-sorted, so we need to go over `n(n-1)/2` operations.|
|Average|`O(n^2)`||