# Convex Hull

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Given a set of n points in the two-dimensional plane, your task is to determine the convex hull of the points.

# Input

The first input line has an integer n: the number of points.

After this, there are n lines that describe the points. Each line has two integers x and y: the coordinates of a point.

You may assume that each point is distinct, and the area of the hull is positive.

# Output

First print an integer k: the number of points in the convex hull.

After this, print k lines that describe the points. You can print the points in any order. Print all points that lie on the convex hull.

# Constraints

- 3 ≤ n ≤ 2 · 10<sup>5</sup>
- -10<sup>9</sup> ≤ x, y ≤ 10<sup>9</sup>

# Example

Input:

```
6
2 1
2 5
3 3
4 3
4 4
6 3
```

Output:

```
4
2 1
2 5
4 4
6 3
```

---
**Source:** [https://cses.fi/problemset/task/2195](https://cses.fi/problemset/task/2195)