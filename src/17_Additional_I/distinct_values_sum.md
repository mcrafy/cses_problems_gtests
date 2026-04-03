# Distinct Values Sum

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given an array x\_1,x\_2,…,x\_n. Let d(a,b) denote the number of distinct values in the subarray x\_a,x\_{a+1},…,x\_b.

Your task is to calculate the sum \sum\_{a=1}^n \sum\_{b=a}^n d(a,b), i.e., the sum of d(a,b) for all subarrays.

# Input

The first line has an integer n: the array size.

The next line has n integers x\_1,x\_2,…,x\_n: the array contents.

# Output

Print one integer: the required sum.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ x\_i ≤ 10<sup>9</sup>

# Example

Input:

```
5
1 2 3 1 1
```

Output:

```
29
```

*Explanation*: In this array, 6 subarrays have 1 distinct value, 4 subarrays have 2 distinct values and 5 subarrays have 3 distinct values. Thus, the sum is 6·1+4·2+5·3=29.

---
**Source:** [https://cses.fi/problemset/task/3150](https://cses.fi/problemset/task/3150)