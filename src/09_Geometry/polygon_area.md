# Polygon Area

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Your task is to calculate the area of a given polygon.

The polygon consists of n vertices (x\_1,y\_1),(x\_2,y\_2),…,(x\_n,y\_n). The vertices (x\_i,y\_i) and (x\_{i+1},y\_{i+1}) are adjacent for i=1,2,…,n-1, and the vertices (x\_1,y\_1) and (x\_n,y\_n) are also adjacent.

# Input

The first input line has an integer n: the number of vertices.

After this, there are n lines that describe the vertices. The ith such line has two integers x\_i and y\_i.

You may assume that the polygon is simple, i.e., it does not intersect itself.

# Output

Print one integer: 2a where the area of the polygon is a (this ensures that the result is an integer).

# Constraints

- 3 ≤ n ≤ 1000
- -10<sup>9</sup> ≤ x\_i, y\_i ≤ 10<sup>9</sup>

# Example

Input:

```
4
1 1
4 2
3 5
1 4
```

Output:

```
16
```

---
**Source:** [https://cses.fi/problemset/task/2191](https://cses.fi/problemset/task/2191)