# K Subset Sums I

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given an array of n integers. Consider the sums of all 2<sup>n</sup> subsets of the given array (including the empty subset with sum equal to zero).

Your task is to find the k smallest subset sums.

# Input

The first line has two integers n and k: the size of the array and the number of subset sums k.

The next line has n integers x\_1, x\_2,…, x\_n: the contents of the array.

# Output

Print k integers: the k smallest subset sums in increasing order.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ k ≤ \min(2<sup>n</sup>, 2 · 10<sup>5</sup>)
- -10<sup>9</sup> ≤ x\_i ≤ 10<sup>9</sup>

# Example

Input:

```
4 9
1 6 3 -3
```

Output:

```
-3 -2 0 0 1 1 3 3 4
```

---
**Source:** [https://cses.fi/problemset/task/3108](https://cses.fi/problemset/task/3108)