# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. Binary Heap Tree](#2-binary-heap-tree)
    - [2.1. Characteristics](#21-characteristics)
    - [2.2. Shapes & Properties](#22-shapes--properties)
    - [2.3. Min-Heap Order](#23-min-heap-order)
    - [2.4. Max-Heap Order](#24-max-heap-order)
    - [2.5. Pros & Cons](#25-pros--cons)
- [3. Operation](#3-operation)
- [4. Efficiencies](#4-efficiencies)
    - [4.1. Time Compleixty compare to other data strucures](#41-time-compleixty-compare-to-other-data-strucures)

<!-- /TOC -->

# 2. Binary Heap Tree

## 2.1. Characteristics
* Follows general shape property of binary tree (max two children per node)
* However, binary heap must be a **complete** binary tree.

## 2.2. Shapes & Properties
* Complete tree
* Implemented with arrays (**index 0 is empty**, 1 is root of the tree)
* For node at index n:
1. left child is at index `(n * 2)`
2. right child is at index `(n * 2) + 1`
3. parent is at index `(n / 2)`

## 2.3. Min-Heap Order
* Minimum heaps keep the **smallest** data in the set at the root.
* Children are always **greater** than the parent, but no relationship between the siblings.
* The last element is at index size.

## 2.4. Max-Heap Order
* Maximum heaps keep the largest data in the set at the root.
* Childrean are always less than the parent (again, no relationship between siblings)
* The last element is at index size.

## 2.5. Pros & Cons
* Can be implemented to use priority queues (from `O(nlogn)` (by inserting and sorting) to `O(logn)` (inserting in `logn` and retrieving in `O(1)`))
* To search an element, you need to search throughout the entire structure. (Time complexity of `O(n)`)

# 3. Operation

* `Build heap tree - O(n)`
1. Get the last internal node (`size / 2`)
2. Swap with siblings with internal node if needed. ("heapify")
3. Go up to the root for every internal node and do the same operation.

* `Add (time complexity = height of the heap = O(logN))`
1. Add an element to the end of the array
2. Compare with parents (`index / 2`) and switch.
3. Repeat the process until it's in the correct relationship with its parent.

* `Remove (time complexity = height of the heap = O(logN))`
1. Delete the index i element that you want to remove.
2. Replace the deleted node with the latest node.
3. Depending on the replacement node value, we need to filter-up or filter-down. (e.g. if min heap, and the replacement node is greater than parent, than filter down.)

> http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/

# 4. Efficiencies
## 4.1. Time Compleixty compare to other data strucures
|Operation|Best Case | Worst Case | Average Case|
|---|---|---|---|
|build| | |`O(n)`|
|search|`O(1)`|`O(n)`|`O(n)`|
|add|`O(1)`|`amortized O(logn)`,`O(n)`|`O(logn)`|
|remove|`O(1)`|`O(logn)`|`O(logn)`|