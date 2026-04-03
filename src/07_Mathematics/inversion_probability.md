# Inversion Probability

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

An array has n integers x\_1,x\_2,…,x\_n, and each of them has been randomly chosen between 1 and r\_i. An inversion is a pair (a,b) where a<b and x\_a>x\_b.

What is the expected number of inversions in the array?

# Input

The first input line contains an integer n: the size of the array.

The second line contains n integers r\_1,r\_2,…,r\_n: the range of possible values for each array position.

# Output

Print the expected number of inversions rounded to six decimal places (rounding half to even).

# Constraints

- 1 ≤ n ≤ 100
- 1 ≤ r\_i ≤ 100

# Example

Input:

```
3
5 2 7
```

Output:

```
1.057143
```

---
**Source:** [https://cses.fi/problemset/task/1728](https://cses.fi/problemset/task/1728)