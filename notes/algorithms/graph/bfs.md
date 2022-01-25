# Bredth-first Search

## Properties
* Use Queue (vertex), Visited Set and starting vertex
```
Function BFS(G, u)
    init visited set VS
    init queue Q
    mark u as visited in VS
    Q.enqueue(u)
    While Q is not empty:
        v <- Q.dequeue()
        for all adjacent vertex w to v:
            if not visited:
                mark w as visited in VS
                Q.enqueue(w)

```

## Efficiencies
`O(|V| + |E|)`

