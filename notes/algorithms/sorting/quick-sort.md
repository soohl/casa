<!-- TOC -->

- [1. Properties](#1-properties)
- [2. Operations](#2-operations)
- [3. Efficiencies](#3-efficiencies)

<!-- /TOC -->
# 1. Properties
* Unstable
* Not Adaptive
* In-place

# 2. Operations
1. Choose an item at random to be the `pivot`.
2. Swap `pivot` with the first item. (Both index and the element) 
3. `left` marker on the next element of the `pivot`, `right` marker on the last item to the right.
4. If element on `left` < element on `pivot`, move `left` one item to the right. 
4. Repeat 4 until `left` element >= `pivot`element  or `left` > `right`. 
5. If element on `right` > element on `pivot`, move `right` one item to the left. 
6. Repeat 6 until `right` element <= `pivot` element or `right` < `left`.
7. After makrers cross-over, swap `pivot` element with `right`.
8. `pivot` is now in the right place (every element on the left is smaller than pivot and every element on the right iois larger than pivot)
9. Perform quick sort on the smaller items and on the larger items. (recursive)

# 3. Efficiencies
|Case|Big O|When|
|---|---|---|
|Best|`O(nlog(n))`|array is perfectly sorted, but still have to go over `nlog(n)` for quick sort|
|Worst|`O(n^2)`|Pivot that is chosen each time will be either min or max value|
|Average|`O(nlog(n))`||