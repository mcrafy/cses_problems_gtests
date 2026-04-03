# Sliding Window Mode

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given an array of n integers. Your task is to calculate the mode each window of k elements, from left to right.

The mode is the most frequent element in an array. If there are several possible modes, choose the smallest of them.

# Input

The first line contains two integers n and k: the number of elements and the size of the window.

Then there are n integers x\_1,x\_2,\ldots,x\_n: the contents of the array.

# Output

Print n-k+1 values: the modes.

# Constraints

- 1 ≤ k ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ x\_i ≤ 10<sup>9</sup>

# Example

Input:

```
8 3
1 2 3 2 5 2 4 4
```

Output:

```
1 2 2 2 2 4
```

---
**Source:** [https://cses.fi/problemset/task/3224](https://cses.fi/problemset/task/3224)