# Sliding Window Mex

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given an array of n integers. Your task is to calculate the mex of each window of k elements, from left to right.

The mex is the smallest nonnegative integer that does not appear in the array. For example, the mex for [3,1,4,3,0,5] is 2.

# Input

The first line contains two integers n and k: the number of elements and the size of the window.

Then there are n integers x\_1,x\_2,\ldots,x\_n: the contents of the array.

# Output

Print n-k+1 values: the mex values.

# Constraints

- 1 ≤ k ≤ n ≤ 2 · 10<sup>5</sup>
- 0 ≤ x\_i ≤ 10<sup>9</sup>

# Example

Input:

```
8 3
1 2 1 0 5 1 1 0
```

Output:

```
0 3 2 2 0 2
```

---
**Source:** [https://cses.fi/problemset/task/3219](https://cses.fi/problemset/task/3219)