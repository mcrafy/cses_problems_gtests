# K Subset Sums Ii

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given an array of n integers. Consider the sums of all \binom{n}{m} subsets of the given array with exactly m elements.

Your task is to find the k smallest subset sums.

# Input

The first line has three integers n, m and k: the size of the array, the size of the subsets and the number of subset sums k.

The next line has n integers x\_1, x\_2,…, x\_n: the contents of the array.

# Output

Print k integers: the k smallest subset sums in increasing order.

# Constraints

- 1 ≤ m < n ≤ 2 · 10<sup>5</sup>
- 1 ≤ k ≤ \min≤ft(\binom{n}{m}, 2 · 10<sup>5</sup>\right)
- -10<sup>9</sup> ≤ x\_i ≤ 10<sup>9</sup>

# Example

Input:

```
5 3 9
-3 1 5 2 0
```

Output:

```
-2 -1 0 2 3 3 4 6 7
```

---
**Source:** [https://cses.fi/problemset/task/3109](https://cses.fi/problemset/task/3109)