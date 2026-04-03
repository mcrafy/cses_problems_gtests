# Fixed-Length Paths Ii

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Given a tree of n nodes, your task is to count the number of distinct paths that have at least k\_1 and at most k\_2 edges.

# Input

The first input line contains three integers n, k\_1 and k\_2: the number of nodes and the path lengths. The nodes are numbered 1,2,\ldots,n.

Then there are n-1 lines describing the edges. Each line contains two integers a and b: there is an edge between nodes a and b.

# Output

Print one integer: the number of paths.

# Constraints

- 1 ≤ k\_1 ≤ k\_2 ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ a,b ≤ n

# Example

Input:

```
5 2 3
1 2
2 3
3 4
3 5
```

Output:

```
6
```

---
**Source:** [https://cses.fi/problemset/task/2081](https://cses.fi/problemset/task/2081)