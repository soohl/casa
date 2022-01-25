# Dijkstra's Graph Algorithm
Find shortest path from source vertex to every other vertex in weighted graph

## Properties
* Works in weighted graph
* **Does not work with negative weights**


### Requirement
* Priority Queue (to hold cumulative distance)
* Visited Set
* Map<V, int> (to hold shortest distance from the source)

## Implementation

```
function dijkstra(G, s):
    init visited set VS
    init distanceMap DM
    init PriorityQueue PQ
    for all V in G, init distance to infinite in DM
    PQ.enque(s, 0)
    while PQ is not empty and VS is full:
        (u, d) <- PQ.dequeue()
        if u is not visited:
            mark u as visited in VS
            update DM for u with new shorted path d
            for all (w, d2) adjacent to u and not visited:
                PQ.enque(w, d + d2)

```
## Efficiencies
`O((|V| + |E|)log|V|)`
