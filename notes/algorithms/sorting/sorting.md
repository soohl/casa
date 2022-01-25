<!-- TOC -->

- [1. Categories](#1-categories)
    - [1.1. Iterative](#11-iterative)
    - [1.2. Diviede & Conquer](#12-diviede--conquer)
- [2. Qualities of sorts](#2-qualities-of-sorts)
    - [2.1. Stability](#21-stability)
    - [2.2. Adaptable](#22-adaptable)
    - [2.3. In-place vs Out-of-place](#23-in-place-vs-out-of-place)

<!-- /TOC -->
# 1. Categories
## 1.1. Iterative
* Bubble Sort
* Insertion Sort
* Selection Sort

## 1.2. Diviede & Conquer
* Merge Sort
* LSD Radix Sort
* Quick Sort

# 2. Qualities of sorts
## 2.1. Stability
* Stable - order of duplicate items is preserved. (e.g. 3A is before 3B) : so, we can apply multiple sorting 
* Un-stable - order of duplicate items may change

## 2.2. Adaptable
* Adaptable - sorting can stop early when the data is sorted

## 2.3. In-place vs Out-of-place
* In-place - no copy over elements into another array or list during sorting (fixed amount of space is used regardless of the size)
* Out-of-place - allocate variable amount of additional space. 
