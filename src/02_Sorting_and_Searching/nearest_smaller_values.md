# Nearest Smaller Values

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Given an array of n integers, your task is to find for each array position the nearest position to its left having a smaller value.

# Input

The first input line has an integer n: the size of the array.

The second line has n integers x\_1,x\_2,…,x\_n: the array values.

# Output

Print n integers: for each array position the nearest position with a smaller value. If there is no such position, print 0.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ x\_i ≤ 10<sup>9</sup>

# Example

Input:

```
8
2 5 1 4 8 3 2 5
```

Output:

```
0 1 0 3 4 3 3 7
```

---
**Source:** [https://cses.fi/problemset/task/1645](https://cses.fi/problemset/task/1645)