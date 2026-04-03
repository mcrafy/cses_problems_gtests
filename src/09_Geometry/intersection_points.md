# Intersection Points

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Given n horizontal and vertical line segments, your task is to calculate the number of their intersection points.

You can assume that no parallel line segments intersect, and no endpoint of a line segment is an intersection point.

# Input

The first line has an integer n: the number of line segments.

Then there are n lines describing the line segments. Each line has four integers: x\_1, y\_1, x\_2 and y\_2: a line segment begins at point (x\_1,y\_1) and ends at point (x\_2,y\_2).

# Output

Print the number of intersection points.

# Constraints

- 1 ≤ n ≤ 10<sup>5</sup>
- -10<sup>6</sup> ≤ x\_1 ≤ x\_2 ≤ 10<sup>6</sup>
- -10<sup>6</sup> ≤ y\_1 ≤ y\_2 ≤ 10<sup>6</sup>
- (x\_1,y\_1) ≠ (x\_2,y\_2)

# Example

Input:

```
3
2 3 7 3
3 1 3 5
6 2 6 6
```

Output:

```
2
```

---
**Source:** [https://cses.fi/problemset/task/1740](https://cses.fi/problemset/task/1740)