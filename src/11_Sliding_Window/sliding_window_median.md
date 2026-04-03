# Sliding Window Median

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given an array of n integers. Your task is to calculate the median of each window of k elements, from left to right.

The median is the middle element when the elements are sorted. If the number of elements is even, there are two possible medians and we assume that the median is the smaller of them.

# Input

The first line contains two integers n and k: the number of elements and the size of the window.

Then there are n integers x\_1,x\_2,\ldots,x\_n: the contents of the array.

# Output

Print n-k+1 values: the medians.

# Constraints

- 1 ≤ k ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ x\_i ≤ 10<sup>9</sup>

# Example

Input:

```
8 3
2 4 3 5 8 1 2 1
```

Output:

```
3 4 5 5 2 1
```

---
**Source:** [https://cses.fi/problemset/task/1076](https://cses.fi/problemset/task/1076)