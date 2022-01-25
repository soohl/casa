# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. Trees](#2-trees)
    - [2.1. Characteristics](#21-characteristics)
    - [2.2. Operations](#22-operations)
- [3. Binary Trees](#3-binary-trees)

<!-- /TOC -->

# 2. Trees
## 2.1. Characteristics
* No cycles (unlike circular linkedList)
* Recursion friendly
* Abstract Data Structures (ADT) - Arrays (not great choice) and LinkedList (preferred)
* Non-linear (hierarchical)
* Types of trees are defined by their **shape** and **order** properties

```
[A]
|----|
[B] [C]
|     |
|     |-----|
[F]  [D]   [E]
```

* `Root` - the entry point for the tree (A)
* `External/leaf nodes` - nodes without children
* `Internal nodes` - nodes with children
* `Children` - the following nodes
1. A is a parent of C, grandparent of D and E
2. B and C are siblings
3. F is cousins of D, E
4. `{C,D,E}` is a subtree of A

* `Depth` - distance of a node from the root (`root = 0`)
* `Height` - distance of a node from the furthest leaf node (`leaf node = 0`); can be calculated recursively by `1 + max(height(childA), height(childB))`.
* `Edge` - pair of nodes such that one is the parent of other or vice versa.
* `Path` -sequence of nodes such that any two consecutive nodes form an edge.

## 2.2. Operations
* **Information methods**:
1. `size()`
2. `isEmpty()`
3. `iterator()`
4. `position()` - returns a list of all node positions

* **Accessor methods**:
1. `root()` - returns `root` of the tree
2. `parent(x)` - returns the `parent` of node `x`
3. `children(x)` - returns the `children` of node `x`
4. `numChild(x)` - returns the number of `children` node `x` has

* **Query methods**:
1. `isInternal()` - called on node
2. `isExternal()`
3. `isRoot()`

# 3. Binary Trees
* Each node can have at most 2 childrens (shape property)
* Each child node is labeled as being either a left or right child

**Each node contains:**
1. `root` - reference to the root
2. `parent` - reference to its parent
3. `left` - reference to left child
4. `right` - reference to right child
5. `data `- content itself
6. `internal` - bool
4. `external` - bool
 