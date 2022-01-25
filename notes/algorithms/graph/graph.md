# Graph

## Properties
* Graph is consisted of set of verticies and edges. 
* `Order(G)` = `|v|` (number of verticies)
* `Size(G)` = `|E|` (number of edges)
* `Degree(V)` = number of edges connected to vertex V

### Undirected graph vs Directed graph
* Undirected - all edges are undirected (no direction)
* Directed - all edges are directed (direction shown by arrow)
* Simple path - shortest path from A to B

### Weight 
* Weight is a cost of traversing an edge

### Sparse VS Dense
* Sparse - number of edge is close to minumum edge
* Dense - number of edge is close to maximum edge

### Connected vs Disconnected graph
* Connected - All vertex are connected via edge
* Disconnected - Two or more nodes of the graph has no path (no edges connected)

**Single vertex is considered connected.** 

### Simple vs Non-simple graph
* Simple graph - no self loop and parallel edge
* Non-simple graph - contain self loop and parallel edge

### Cyclic vs Acyclic graph
* Cyclic - cycle exists in the graph (e.g. starting from A, we can traverse back to A)
* Acyclic - cycle does not exists in the graph

**Connected, Acyclic graph is considered tree.**

## How to store graph information?
* Adjanceny matrix 
    - Space Complexity: `O(|V|^2)`
    - Not efficient when adding new vertex
* Adjancency list
    - Space Complexity: `O(|V| + |E|)`
    - Good for sparse graph
* Edge list
    - Space Complexity: `O(|E|)` (no vertex information)
    - No way to represent isolated verticies


