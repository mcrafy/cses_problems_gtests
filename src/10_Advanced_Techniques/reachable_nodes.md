# Reachable Nodes

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

A directed acyclic graph consists of n nodes and m edges. The nodes are numbered 1,2,…,n.

Calculate for each node the number of nodes you can reach from that node (including the node itself).

# Input

The first input line has two integers n and m: the number of nodes and edges.

Then there are m lines describing the edges. Each line has two distinct integers a and b: there is an edge from node a to node b.

# Output

Print n integers: for each node the number of reachable nodes.

# Constraints

- 1 ≤ n ≤ 5 · 10<sup>4</sup>
- 1 ≤ m ≤ 10<sup>5</sup>

# Example

Input:

```
5 6
1 2
1 3
1 4
2 3
3 5
4 5
```

Output:

```
5 3 2 2 1
```

---
**Source:** [https://cses.fi/problemset/task/2138](https://cses.fi/problemset/task/2138)