# Distinct Values Splits

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given an array of n integers. Your task is to count the number of ways to split the array into continuous segments such that all segments consists of distinct values.

# Input

The first line has an integers n: the size of the array.

The next line has n integers x\_1, x\_2,…, x\_n: the contents of the array.

# Output

Print one integer: the answer to the problem modulo 10<sup>9</sup> + 7.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ x\_i ≤ 10<sup>9</sup>

# Example

Input:

```
4
1 2 1 3
```

Output:

```
6
```

*Explanation*: There are six valid splits:

- [1], [2], [1], [3]
- [1], [2], [1, 3]
- [1], [2, 1], [3]
- [1], [2, 1, 3]
- [1, 2], [1], [3]
- [1, 2], [1, 3]

---
**Source:** [https://cses.fi/problemset/task/3190](https://cses.fi/problemset/task/3190)