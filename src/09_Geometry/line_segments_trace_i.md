# Line Segments Trace I

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

There are n line segments whose endpoints have integer coordinates. The left x-coordinate of each segment is 0 and the right x-coordinate is m. The slope of each segment is an integer.

For each x-coordinate 0,1,…,m, find the maximum point in any line segment.

# Input

The first line has two integers n and m: the number of line segments and the maximum x-coordinate.

The next n lines describe the line segments. Each line has two integers y\_1 and y\_2: there is a line segment between points (0,y\_1) and (m,y\_2).

# Output

Print m+1 integers: the maximum points for x=0,1,…,m.

# Constraints

- 1 ≤ n, m ≤ 10<sup>5</sup>
- 0 ≤ y\_1,y\_2 ≤ 10<sup>9</sup>

# Example

Input:

```
4 5
1 6
7 2
5 5
10 0
```

Output:

```
10 8 6 5 5 6
```

---
**Source:** [https://cses.fi/problemset/task/3427](https://cses.fi/problemset/task/3427)