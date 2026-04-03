# Distinct Colors

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given a rooted tree consisting of n nodes. The nodes are numbered 1,2,\ldots,n, and node 1 is the root. Each node has a color.

Your task is to determine for each node the number of distinct colors in the subtree of the node.

# Input

The first input line contains an integer n: the number of nodes. The nodes are numbered 1,2,\ldots,n.

The next line consists of n integers c\_1,c\_2,\ldots,c\_n: the color of each node.

Then there are n-1 lines describing the edges. Each line contains two integers a and b: there is an edge between nodes a and b.

# Output

Print n integers: for each node 1,2,\ldots,n, the number of distinct colors.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ a,b ≤ n
- 1 ≤ c\_i ≤ 10<sup>9</sup>

# Example

Input:

```
5
2 3 2 2 1
1 2
1 3
3 4
3 5
```

Output:

```
3 1 2 1 1
```

---
**Source:** [https://cses.fi/problemset/task/1139](https://cses.fi/problemset/task/1139)