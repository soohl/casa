# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. AVL Trees](#2-avl-trees)
    - [2.1. Rotations](#21-rotations)
        - [2.1.1. Left Rotations (right right case)](#211-left-rotations-right-right-case)
        - [2.1.2. Right Rotations (left left case)](#212-right-rotations-left-left-case)
        - [2.1.3. Left-Right Rotation (left right case)](#213-left-right-rotation-left-right-case)
        - [2.1.4. Right-Left Rotation (right left case)](#214-right-left-rotation-right-left-case)
    - [2.2. Update Height and Balance Factor](#22-update-height-and-balance-factor)
    - [2.3. Insertion](#23-insertion)
    - [Removal](#removal)

<!-- /TOC -->

# 2. AVL Trees
* AVLs are subset of binary search trees (`BST`)
    * Order property is the same (left subtree < parent < right subtree)
    * Add and remove are relatively the same
* AVLs self-balence to eliminate the worst case degenerate tree
    * All AVL operations are `O(log n)` even in the worst case
* AVL nodes store the `data`, `left child`, `right child`, `height` and `balance factor`.
    * **Balance Factor** = `left child height - right child height`
    * The height of a `null` node is `-1`.
    * The height and balance factor of any leaf node is 0. `((-1) - (-1) = 0)`
    * If `BF < -1` OR `BF > 1` = the node is imbalanced
    * If `-1 <= BF <= 1` = the node is balanced enough
    * If `BF < 0` = right heavy
    * If `BF > 0` = left heavy

## 2.1. Rotations
Rotations is used to fix imbalances. There are 4 possible rotations:
* **Left Rotation** *(single rotation)*
* **Right Rotation** *(single rotation)*
* **Left-Right Rotation** *(double rotation)*
* **Right-Left Rotation** *(double rotation)*

**When to use what rotation?**

We want to add a new node `W`.
* `Z` = first unbalanced node
* `Y` = child of `Z` that comes the path from `W` to `Z`.
* `X` = grandchild of `Z` that comes the path from `W` to `Z`. (may equal `W`)

1. `Y` is a right child of `Z` and `X` is a right chid of `Y` : Left Rotations
2. `Y` is a left child of `Z` and `X` is left child of `Y` : Right Rotations
3. `Y` is a right child of `Z` and `X` is a left child of `Y` : Right-Left Rotations
4. `Y` is a left child of `Z` and `X` is a right child of `Y` : Left-Right Rotations

**Based on balancing factor...**

|Parent BF|Left BF|Right BF|Rotation that should be used|
|---|---|---|---|
|-2| |-1 OR 0|Left (right right case)|
|2|1 OR 0| |Right (left left case)|
|2|-1| |Left-Right (left right case)|
|-2| |1|Right-Left (right left case)|

**Determine rotation cases**
```
If abs(bf) > 1: // Not balanced

    If node is left heavy (bf > 0): // Right OR Left-Right

        If node.left is right heavy (node.left.bf < 0): // Left-Right
            do left rotation on node.left
            do right rotation on node

        Else (node.left.bf >= 0): // Right
            do right rotation on node

    Else (node is right heavy (bf < 0)): // Left OR Right-Left

        If node.right is left heavy (node.right.bf > 0): // Right-Left
            do right rotation on node.right
            do left rotation on node
        
        Else (node.right.bf < 0): // Left
            do left rotation on node
```

### 2.1.1. Left Rotations (right right case)
```
Added *C to the tree, making it unbalanced.

    A(-2)                                    
      \                                        B(0)
       B(-1)   -----> left Rotation ----->     /   \
        \                                  A(0) *C(0)
        *C(0)
```

1. Go up the tree from `*C` to the closest unbalanced node `A`
2. Apply left rotation to `A` - `rotateLeft(A)`.
3. The tree is balanced. 

```
AVLNode rotateLeft (AVLNode a) {
    AVLNode b = a.getRight();
    a.setRight(b.getLeft());
    b.setLeft(a);
    update(a); // a is not a child of b.
    update(b); // updating b relies on update(a)
    return b;
}
```

### 2.1.2. Right Rotations (left left case)
```
Added *C to the tree, making it unbalanced.

    A(2)                                    
    /                                    B(0)
   B(1)   -----> Right Rotation ----->  /   \
   /                                  *C(0) A(0)
 *C(0)
```
1. Go up the tree from `*C` to the closest unbalanced node `A`.
2. Apply right rotation to `A` - `rotateRight(A)`.
3. The tree is balanced. 
```
AVLNode rotateRight (AVLNode a) {
    AVLNode b = a.getLeft();
    a.setLeft(b.getRight());
    b.setRight(a);
    update(a); 
    update(b);
    return b;
}
```

### 2.1.3. Left-Right Rotation (left right case)
```
Added *C to the tree, making it unbalanced.

     A(2)                           A(2)                                
     /                              /                            C*(0)
   B(-1)  --> Left Rotation -->  C*(1)  --> Right Rotation -->   /  \
     \                            /                            B(0) A(0)
    *C(0)                       B(0)

```
1. Go up the tree from `*C` to the closest unbalanced node `A`
2. Apply left rotation to left subtree of `A` - `rotateLeft(B)`. 
2. Apply right rotation to `A` - `rotateRight(A)`.
3. The tree is balanced. 

### 2.1.4. Right-Left Rotation (right left case)
```
Added *C to the tree, making it unbalanced.

    A(-2)                            A(-2)                                
       \                               \                            C*(0)
       B(1)  --> Right Rotation -->  C*(-1)  --> Left Rotation -->  /  \
       /                                 \                        A(0) B(0) 
    *C(0)                                B(0)

```
1. Go up the tree from `*C` to the closest unbalanced node `A`
2. Apply right rotation to right subtree of `A` - `rotateRight(B)`. 
2. Apply left rotation to `A` - `rotateLeft(A)`.
3. The tree is balanced. 

## 2.2. Update Height and Balance Factor
After the rotation, the height and balance factor of associated node must be updated.
``` 
// Update Height and Balancing factor of a specific node
private void updateHnBF(AVL Node<T> node) {
    node.bf = easyH(node.left) - easyH(node.right);
    node.height = 1 + Math.max(easyH(node.left), easyH(node.right));
}

// Return -1 for null node 
private int easyH(AVL Node<T> node) {
        if (node == null) {return -1;}
        else {return node.height;}
}
```
## 2.3. Insertion
1. Add element like BST addition.
2. On the way back up the recursive stack (by tracing back through the parents up to the root), update the heights and balance factors. 
3. If the new balance factor show `out of balance`, perform a rotation based on its balance factor.

## Removal
1. Remove the node like BST remobal (0,1,2 child cases)
2. Update height and the balance factor of all the nodes that we visited while traversal.
3. Perform rotation based on the balance factor. (single or maybe multiple rotation required)