# Two Array Average

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given two arrays of n integers.

Your task is to select a nonempty prefix from both arrays such that the average of all selected numbers is as large as possible.

# Input

The first line has an integer n.

The second line has n integers a\_1,a\_2,…,a\_n: the numbers in the first array.

The third line has n integers b\_1,b\_2,…,b\_n: the numbers in the second array.

# Output

Print two numbers: the prefix sizes.

Your answer is considered correct if the absolute or relative difference to the maximum average is at most 10^{-6}.

# Constraints

- 1 ≤ n ≤ 10<sup>5</sup>
- 1 ≤ a\_i, b\_i ≤ 10<sup>9</sup>

# Example

Input:

```
4
1 5 5 2
3 1 3 1
```

Output:

```
3 1
```

Explanation: if you choose the prefixes [1,5,5] and [3], the average is (1+5+5+3)/4=3.5 which is the maximum possible average.

---
**Source:** [https://cses.fi/problemset/task/3361](https://cses.fi/problemset/task/3361)