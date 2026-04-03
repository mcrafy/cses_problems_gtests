# K Subset Xors

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given an array of n integers. Consider the xors of all 2<sup>n</sup> subsets of the array (including the empty subset with xor equal to zero).

Your task is to find the k smallest subset xors.

# Input

The first line has two integers n and k: the size of the array and the number of subset xors k.

The next line has n integers x\_1, x\_2,…, x\_n: the contents of the array.

# Output

Print k integers: the k smallest subset xors in increasing order.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ k ≤ \min(2<sup>n</sup>, 2 · 10<sup>5</sup>)
- 0 ≤ x\_i ≤ 10<sup>9</sup>

# Example

Input:

```
4 9
3 5 14 8
```

Output:

```
0 0 3 3 5 5 6 6 8
```

---
**Source:** [https://cses.fi/problemset/task/3192](https://cses.fi/problemset/task/3192)