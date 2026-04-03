# Sliding Window Advertisement

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

A fence consists of n vertical boards. The width of each board is 1 and their heights may vary.

You want to attach a rectangular advertisement to the fence. Your task is to calculate the maximum area of such an advertisement in each window of k vertical boards, from left to right.

# Input

The first line contains two integers n and k: the width of the fence and the size of the window.

After this, there are n integers x\_1, x\_2, …, x\_n: the height of each board.

# Output

Print n - k + 1 integers: the maximum areas of the advertisements.

# Constraints

- 1 ≤ k ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ x\_i ≤ 10<sup>9</sup>

# Example

Input:

```
8 3
4 1 5 3 3 2 4 1
```

Output:

```
5 6 9 6 6 4
```

---
**Source:** [https://cses.fi/problemset/task/3227](https://cses.fi/problemset/task/3227)