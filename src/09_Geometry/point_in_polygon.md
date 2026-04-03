# Point In Polygon

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given a polygon of n vertices and a list of m points. Your task is to determine for each point if it is inside, outside or on the boundary of the polygon.

The polygon consists of n vertices (x\_1,y\_1),(x\_2,y\_2),…,(x\_n,y\_n). The vertices (x\_i,y\_i) and (x\_{i+1},y\_{i+1}) are adjacent for i=1,2,…,n-1, and the vertices (x\_1,y\_1) and (x\_n,y\_n) are also adjacent.

# Input

The first input line has two integers n and m: the number of vertices in the polygon and the number of points.

After this, there are n lines that describe the polygon. The ith such line has two integers x\_i and y\_i.

You may assume that the polygon is simple, i.e., it does not intersect itself.

Finally, there are m lines that describe the points. Each line has two integers x and y.

# Output

For each point, print "INSIDE", "OUTSIDE" or "BOUNDARY".

# Constraints

- 3 ≤ n,m ≤ 1000
- 1 ≤ m ≤ 1000
- -10<sup>9</sup> ≤ x\_i, y\_i ≤ 10<sup>9</sup>
- -10<sup>9</sup> ≤ x, y ≤ 10<sup>9</sup>

# Example

Input:

```
4 3
1 1
4 2
3 5
1 4
2 3
3 1
1 3
```

Output:

```
INSIDE
OUTSIDE
BOUNDARY
```

---
**Source:** [https://cses.fi/problemset/task/2192](https://cses.fi/problemset/task/2192)