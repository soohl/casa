# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. Skip Lists](#2-skip-lists)
    - [2.1. Structures](#21-structures)
        - [2.1.1. Single Node](#211-single-node)
        - [2.1.2. Levels](#212-levels)
    - [2.2. Functions & Features](#22-functions--features)
    - [2.3. Operations](#23-operations)
        - [2.3.1. Searching](#231-searching)
    - [2.4. Efficiencies](#24-efficiencies)
        - [2.4.1. Time Complexity](#241-time-complexity)
        - [2.4.2. Space Complexity](#242-space-complexity)

<!-- /TOC -->

# 2. Skip Lists

## 2.1. Structures
### 2.1.1. Single Node
```
         ---------
         | above |
  -----------------------
  | prev | *data | next |
  -----------------------
         | below |
         ---------
```
### 2.1.2. Levels
Levels are made up of "linked lists" of nodes, all the data can be found at the lowest level (level 0), but elements will be promoted at random to higher levels
* We will use coin fliper to determine if an element is promoted, we'll promte when heads is flipped and stop when tails is flipped

*Example)*
* The probability of data being promoted `1` level is `1/2`
* The probability of data being promoted `2` level is `1/4`
* The probability of data being promoted `3` level is `1/8`

1. **T** : data is only on level 0
2. **HT**: data is on level 0 and 1
3. **HHT**: data is on level 0, 1, 2 

> Levels are bounded by negative infinity and postive infinity as the "head" and "tail" - data elements are placed in order at each level. 

## 2.2. Functions & Features
* The goal of a skipList is to be able to skip over data while traversing to allow us to search for elements very quickly
* skipLists are unique because they employ randomization

*Example)*
Add `{13,17,20,45}` with the coin flips `{HTTHHHTHHT}` or `{1001110110}`
1. `13(HT)` is added at levels 0,1
2. `17(T)` is only added at level 0
3. `20(HHHT)` is added at levels 0,1,2,3
4. `45(HHT)` is added at levels 0,1,2
```
Level 3: [-∞] --------------- [20] -------- [+∞]
Level 2: [-∞] --------------- [20] - [45] - [+∞]
Level 1: [-∞] - [13] -------- [20] - [45] - [+∞]
Level 0: [-∞] - [13] - [17] - [20] - [45] - [+∞] 
*Nodes are connected between levels as well. 
```
*When you are not adding in order (from smallest to largest), you need to search the element first and add on the right of the end node.*

## 2.3. Operations

### 2.3.1. Searching
Starting at the top left negative infinity node as the current node.
* Compare the data you want to the data to the right of current
    * If the `data.right > data you want` : Set `current node` to `BELOW` of current node
    * When **adding**, if `BELOW` is `null`, don't update current, the data belongs to the right of current
    * If the `data.right < data you want` : Set `current node` to `RIGHT` of current node
* Repeat until you find your data or hit `null`.



## 2.4. Efficiencies
**Best Case)** `1/2` the data on level 1, `1/4` the data on level 2 etc.

**Worst Case)** all the data is on every level. (top level is like linked list)

### 2.4.1. Time Complexity
|Operation|Best Case|Worst Case|Average Case|
|---|---|---|---|
|add|`O(log n)`|`O(n)`|`O(log n)`|
|search|`O(log n)`|`O(n)`|`O(log n)`|
|remove|`O(log n)`|`O(n)`|`O(log n)`|

### 2.4.2. Space Complexity
|Operation|Best Case|Worst Case|Average Case|
|---|---|---|---|
|space|`O(1)`|`O(nlogn)`|`O(n)`|
