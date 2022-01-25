# Prim's algorithm
To find minimum spanning tree of the graph

## Terminology
* Tree : an acyclic, connected, undirected graph
* Spanning Tree : A tree that connects every vertex in the graph
* Minimum Spanning Tree (MST) : A spanning tree with the smallest total edge weight
* Subgraph(G) : Graph whose all set of verticies and edges are all subset of G

## Properties
* Graph Cut - A graph cut takes a subset of the verticies and all edges connecting them
* Any MST **must** include minimum edge connecting two subgraphs left by and graph cut
* Prim's algorithm is a greedy algorithm (builds the MST one vertex at a time)
* Similar to djkstra
**Multiple MST can exist for given graph.**

### Requirement
* Visisted Set
* Priority Queue (edge, weight of the edge)
* MST Edge Set (edge in MST) 
* Next edge dequeued from PQ represents shortest path found in the graph cut
* Edges of minimum weight that are traversed are stored in MST set

## Implementation
```
function prim(G, s):
    init visited set VS
    init MST edge set 
    init priority queue PQ
    for each edge (s,v) in G, PQ.enqueue(edge(s,v))
    mark s as visited in VS
    while PQ is not empty and VS is not full:
        edge(u,v) <- PQ.dequeue()
        if v is not visited in VS:
            mark v as visited in VS
            add edge(u, v) to MST set
            for each edge(v, x) such x is not visited:
                PQ.enqueue(edge(v,x))
```
## Efficiencies
`O((|V| + |E|)log|V|)`
