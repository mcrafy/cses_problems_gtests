# Range Interval Queries

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Given an array x of n integers, your task is to process q queries of the form: how many integers i satisfy a ≤ i ≤ b and c ≤ x\_i ≤ d?

# Input

The first line has two integers n and q: the number of values and queries.

The second line has n integers x\_1,x\_2,…,x\_n: the array values.

Finally, there are q lines describing the queries. Each line has four integers a, b, c and d: how many integers i satisfy a ≤ i ≤ b and c ≤ x\_i ≤ d?

# Output

Print the result of each query.

# Constraints

- 1 ≤ n,q ≤ 2 · 10<sup>5</sup>
- 1 ≤ x\_i ≤ 10<sup>9</sup>
- 1 ≤ a ≤ b ≤ n
- 1 ≤ c ≤ d ≤ 10<sup>9</sup>

# Example

Input:

```
8 4
3 2 4 5 1 1 5 3
2 4 2 4
5 6 2 9
1 8 1 5
3 3 4 4
```

Output:

```
2
0
8
1
```

---
**Source:** [https://cses.fi/problemset/task/3163](https://cses.fi/problemset/task/3163)