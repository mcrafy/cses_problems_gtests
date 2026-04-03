# Distinct Values Subsequences

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Given an array of n integers, count the number of subsequences where each element is distinct.

A subsequence is a sequence of array elements from left to right that may have gaps.

# Input

The first line has an integer n: the array size.

The second line has n integers x\_1,x\_2,…,x\_n: the array contents.

# Output

Print the number of subsequences with distinct elements. The answer can be large, so print it modulo 10<sup>9</sup>+7.

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
11
```

*Explanation*: The subsequences are [1] (two times), [2], [3], [1,2], [1,3] (two times), [2,1], [2,3], [1,2,3] and [2,1,3].

---
**Source:** [https://cses.fi/problemset/task/3421](https://cses.fi/problemset/task/3421)