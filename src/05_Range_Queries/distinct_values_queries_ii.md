# Distinct Values Queries Ii

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Given an array of n integers, your task is to process q queries of the following types:

1. update the value at position k to u
2. check if every value in range [a, b] is distinct

# Input

The first line has two integers n and q: the number of values and queries.

The second line has n integers x\_1, x\_2,…, x\_n: the array values.

Finally, there are q lines describing the queries. Each line has three integers: either "1 k u" or "2 a b".

# Output

For each query of type 2, print `YES` if every value in the range is distinct and `NO` otherwise.

# Constraints

- 1 ≤ n, q ≤ 2 · 10<sup>5</sup>
- 1 ≤ x\_i, u ≤ 10<sup>9</sup>
- 1 ≤ k ≤ n
- 1 ≤ a ≤ b ≤ n

# Example

Input:

```
5 4
3 2 7 2 8
2 3 5
2 2 5
1 2 9
2 2 5
```

Output:

```
YES
NO
YES
```

---
**Source:** [https://cses.fi/problemset/task/3356](https://cses.fi/problemset/task/3356)