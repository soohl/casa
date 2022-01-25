# Kruskal's algorithm
Find MST of the graph

## Properties
* Works with connected or disconnected graph
* Maintain clusters of the graph

### Requirements
* Priority queue of edges
* Cluster / disjoint set
* MST edge set


## Implementation
```
function kruskal(G):
    init disjoint set DS, with all V in G
    init MST edge set
    init priority queue PQ with all edges in G
    while PQ is not empty and MST has fewer then n-1 edges:
        edge(u, v) <- PQ.deque()
        if u and v are not in same cluster in DS:
            add edge(u, v) to MST set
            merge u's cluster with v's
```

## Efficiencies
`O(|E|log|V|)`
