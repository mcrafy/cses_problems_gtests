# Sliding Window Distinct Values

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given an array of n integers. Your task is to calculate the number of distinct values in each window of k elements, from left to right.

# Input

The first line contains two integers n and k: the number of elements and the size of the window.

Then there are n integers x\_1,x\_2,\ldots,x\_n: the contents of the array.

# Output

Print n-k+1 values: the numbers of distinct values.

# Constraints

- 1 ≤ k ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ x\_i ≤ 10<sup>9</sup>

# Example

Input:

```
8 3
1 2 3 2 5 2 2 2
```

Output:

```
3 2 3 2 2 1
```

---
**Source:** [https://cses.fi/problemset/task/3222](https://cses.fi/problemset/task/3222)