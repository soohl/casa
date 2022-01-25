# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. Binary Search Tree (BST)](#2-binary-search-tree-bst)
    - [2.1. Characteristics](#21-characteristics)
    - [2.2. Advantages](#22-advantages)
    - [2.3. Shapes](#23-shapes)
- [3. Traversal](#3-traversal)
    - [3.1. Depth-firsts (recursive)](#31-depth-firsts-recursive)
        - [3.1.1. Preorder (CLR)](#311-preorder-clr)
        - [3.1.2. Postorder (LRC)](#312-postorder-lrc)
        - [3.1.3. Inorder()](#313-inorder)
    - [3.2. Breadth-firsts (not recursive)](#32-breadth-firsts-not-recursive)
        - [3.2.1. Level order](#321-level-order)
- [4. Insertion](#4-insertion)
- [5. Removal](#5-removal)
    - [5.1. No Children](#51-no-children)
    - [5.2. One Children](#52-one-children)
    - [5.3. Two Children](#53-two-children)
- [6. Efficiencies](#6-efficiencies)
    - [6.1. Time Compleixty](#61-time-compleixty)

<!-- /TOC -->

# 2. Binary Search Tree (BST)
## 2.1. Characteristics
* Binary tree property + order property
* Data in left subtree < current node's data
* Data in rught subtree > current node's data
* Data must be Comparable (must implement Comparable interface that requires the implementation of the .compareTo() method)
1. If `a.compareTo(b) < 0` : `a < b`
2. If `a.compareTo(b) > 0` : `a > b`

## 2.2. Advantages
* Optimized for searching (traverse few nodes to find a data since we can eliminate the half of the tree for each comparision)

## 2.3. Shapes
* **Full** - all node have o or 2 children
* **Complete** - leaves are filled in level by level, from left to right -> no gaps
* **Degenerate** - worst case tree -> as implemented with linkedlist

# 3. Traversal
## 3.1. Depth-firsts (recursive)
### 3.1.1. Preorder (CLR)
```
Read node()
Recurse left()
Recurse right()
```
### 3.1.2. Postorder (LRC)
```
Recurse left()
Recurse right()
Read node()
```
### 3.1.3. Inorder()
```
Recurse left()
Read node()
Recurse right()
```

## 3.2. Breadth-firsts (not recursive)
### 3.2.1. Level order
1. Add root to queue
2. While the queue is not empty:
    1. Remove one node from the queue
    2. Enque its left and right children (in this order)

# 4. Insertion
1. Traverse like searching the node

```
void add(data)
    root = add(data, node);

Node add(data, node) {
    if (node == null)
        return new Node(data);
    else if (data < node.data) 
        node.left = add (data, node.left);
    else if (data > node.data)
        node.right = add(data, node.right);
    return node;
}
```

# 5. Removal
The removal strategy of BST depends on the number of children of the node that wanted to be removed. 

## 5.1. No Children
1. Set parent's pointer to the null.
## 5.2. One Children
1. Set the parent's pointer to the node to the node's child
## 5.3. Two Children
1. Replace the node's data with either predecessor or successor (predecessor - largest value on the left subtree, successor - smallest value on the right subtree)
2. Remove the predecessor or successor (either no children or one children)

# 6. Efficiencies
## 6.1. Time Compleixty
|Operation|Best Case | Worst Case | Average Case|
|---|---|---|---|
|height|`O(1)`|`O(n)`|`O(logn)`|
|search|`O(1)`|`O(n)`|`O(logn)`|
|add|`O(1)`|`O(n)`|`O(logn)`|
|remove|`O(1)`|`O(n)`|`O(logn)`|