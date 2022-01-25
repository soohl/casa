<!-- TOC -->

- [1. Properties](#1-properties)
    - [1.1. Order Properties](#11-order-properties)
    - [1.2. Size properties](#12-size-properties)
    - [1.3. Shape properties](#13-shape-properties)
- [2. Operations](#2-operations)
    - [2.1. Insertion](#21-insertion)
        - [2.1.1. Easy Case](#211-easy-case)
        - [2.1.2. Hard Case - Overflow](#212-hard-case---overflow)
        - [2.1.3. Solving overflow (promotion / splitting)](#213-solving-overflow-promotion--splitting)
        - [2.1.4. Splitting non-root node](#214-splitting-non-root-node)
        - [2.1.5. Splitting parent node](#215-splitting-parent-node)
    - [2.2. Removal](#22-removal)
        - [2.2.1. Removing data in a leaf node](#221-removing-data-in-a-leaf-node)
        - [2.2.2. Removing data in internal node](#222-removing-data-in-internal-node)
        - [2.2.3. Fusion](#223-fusion)
        - [2.2.4. Transfer](#224-transfer)
- [Efficiencies](#efficiencies)
    - [Time Complexity](#time-complexity)

<!-- /TOC -->

# 1. Properties

## 1.1. Order Properties
* Each node stores values sorted from smallest to greatest

## 1.2. Size properties
* Each node can store 1 to 3 data values
* Internal node can have `2 to 4` children
* External node can store 1 to 3 data values but can not have children
* Internal node with `m` children must have `m+1` data values

## 1.3. Shape properties
* All leaf nodes are at the same height(perfectly balanced)

# 2. Operations

## 2.1. Insertion
* **New elements are inserted only in leaf nodes**

### 2.1.1. Easy Case
*Example)* Insert {4,12,6}
```     
            *root
            [null]
insert(4):  [null] -> [4| | ]
insert(12): [null] -> [4|12| ]
insert(6):  [null] -> [4|6|12]
```
1. Inserting data in to the first node is easy.
2. Just simply add to the node from smallest to biggest.

### 2.1.2. Hard Case - Overflow
*Example)* Insert {5} 
```     
            *root
            [null] -> [4|6|12]
insert(15): [null] -> [4|6|12|15] *X: Not possible since single node can hold maximum 3 data value*
```
1. Single node can not hold more than 3 data values. 
2. We need to use special technique to solve overflow problem.

### 2.1.3. Solving overflow (promotion / splitting)
```
//////////// 1 //////////////

*root
[null] -> [4|6|12|15]
         c1 c2 c3 c4 c5

//////////// 2 //////////////

[null] -> [4|6| ]    (12) : Leave out the middle value  
[newNode] -> [15| | ]

//////////// 3 //////////////

[null] -> [12| | ]
          /   \
    [4|6| ]   [15| | ]
  c1 c2 c3    c4 c5
```
1. For now, we will keep the 4th entry `15`. 
2. `c1`,`c2`,`c3`,`c4`,`c5` are references (pointer) to children. 
3. Leave out the middle value (6 or 12, it does not matter)
4. Create a new node and copy `{c4, 15, c5}`
5. Create a new node using middle value `12`
6. Make the the other two tree, the subtree of `12` containing node. 

**The height of the node increases by 1 when split**

### 2.1.4. Splitting non-root node
Insert `{3,5}`
```
insert(3)
insert(5)

[null] -> [12| | ]
          /   \
    [3|4|5|6] [15| | ]
 c1 c2 c3 c4 c5

///////////////////////////

[null] -> [12| | ]
          /   \
    [3|4| ]   [15| | ]    (5): Leave out 
 c1 c2 c3 null

[q] ->  [6| | ]
       p4 p5 null null

///////////////////////////
           e3 q 
[null] ->  [5|12| ]
          /   |   \
     [3|4| ] [6| | ] [15| | ]   
            p4 p5
```
1. Overflow occurs on non-root node
2. Leave out the middle value (4 or 5)
3. Create new node and copy `{c4, 6, c5}`
4. Insert left over entry (5) into the parent node and the new node as it's right subtree.

### 2.1.5. Splitting parent node
```
[null]  ->    [ 5 | 10 | 12 | 15 ]
            /     |    |    |      \
     [3|4| ]  [6|8|] [11||] [13|14|] [17| | ]

////////////////////////////////////////

[5|10| ]    (12)     [15| | ]
c1 c2 c3             c4 c5

////////////////////////////////////////

            [     12     |  |  ]
           /              \
      [5|10| ]           [15| | ]
     /  |   \           /    \
[3|4| ] [6|8|] [11||] [13|14|] [17| | ]
```
1. When the root with children node is overflowing...
2. Leave out middle value (12)
3. Split node and create new node `[15| | ]`
4. Create a new node containing left out `[12| | ]`
5. Set left pointer to the original node
5. Set right pointer to the new node. 

## 2.2. Removal

### 2.2.1. Removing data in a leaf node
1. Remove the data
2. If that creates underflow on root node (create a node with zero data entries), remove empty root node and set new root to root's only child.
3. If does not create an underflow, its done.

### 2.2.2. Removing data in internal node
1. Remove and replace the data in its node with predecessor or successor data
2. Remove predecessor or successor data from node you got it from. 
2. If that creates underflow on root node (create a node with zero data entries), remove empty root node and set new root to root's only child.
3. If does not create an underflow, its done.

### 2.2.3. Fusion

### 2.2.4. Transfer

# Efficiencies
## Time Complexity
|Operation|Best Case | Worst Case | Average Case|
|---|---|---|---|
|search|`O(1)`|`O(logn)`|`O(logn)`|
|add|`O(1)`|`O(logn)`|`O(logn)`|
|remove|`O(1)`|`O(logn)`|`O(logn)`|