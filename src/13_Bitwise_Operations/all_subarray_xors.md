# All Subarray Xors

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Given an array of n integers, your task is to find all integers that are the xor sum in some subarray.

# Input

The first line has an integer n: the size of the array.

The next line has n integers x\_1,x\_2,…,x\_n: the contents of the array.

# Output

First print an integer k: the number of distinct integers that are the xor sum in some subarray.

After this print k integers: the xor sums in increasing order.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- 0 ≤ x\_i ≤ 10<sup>6</sup>

# Example

Input:

```
4
5 1 5 9
```

Output:

```
7
1 4 5 8 9 12 13
```

---
**Source:** [https://cses.fi/problemset/task/3233](https://cses.fi/problemset/task/3233)