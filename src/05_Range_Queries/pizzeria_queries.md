# Pizzeria Queries

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

There are n buildings on a street, numbered 1,2,…,n. Each building has a pizzeria and an apartment.

The pizza price in building k is p\_k. If you order a pizza from building a to building b, its price (with delivery) is p\_a+|a-b|.

Your task is to process two types of queries:

1. The pizza price p\_k in building k becomes x.
2. You are in building k and want to order a pizza. What is the minimum price?

# Input

The first input line has two integers n and q: the number of buildings and queries.

The second line has n integers p\_1,p\_2,…,p\_n: the initial pizza price in each building.

Finally, there are q lines that describe the queries. Each line is either "1 k x" or "2 k".

# Output

Print the answer for each query of type 2.

# Constraints

- 1 ≤ n,q ≤ 2 · 10<sup>5</sup>
- 1 ≤ p\_i, x ≤ 10<sup>9</sup>
- 1 ≤ k ≤ n

# Example

Input:

```
6 3
8 6 4 5 7 5
2 2
1 5 1
2 2
```

Output:

```
5
4
```

---
**Source:** [https://cses.fi/problemset/task/2206](https://cses.fi/problemset/task/2206)