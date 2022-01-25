# Depth-First Search
Traverse all verticies in the graph in depth-first fashion

## Properties
* Non-recursive or recursive implementation

### Non-Recursive
* Use Stack, Visited Set and Starting Vertex

### Recursive
```
Function DFS(G, u)
    add u to Visited Set
    for all adjacent vertex w of u:
        if w is not visited:
            DFS(G, w)
```

## Efficiencies
`O(|V| + |E|)`
