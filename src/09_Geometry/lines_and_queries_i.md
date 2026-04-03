# Lines And Queries I

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Your task is to efficiently process the following types of queries:

1. Add a line ax+b
2. Find the maximum point in any line at position x

# Input

The first line has an integer n: the number of queries.

The following n lines describe the queries. The format of each line is either "1 a b" or "2 x".

You may assume that the first query is of type 1.

# Output

Print the answer for each query of type 2.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- -10<sup>9</sup> ≤ a,b ≤ 10<sup>9</sup>
- 0 ≤ x ≤ 10<sup>5</sup>

# Example

Input:

```
6
1 1 2
2 1
2 3
1 0 4
2 1
2 3
```

Output:

```
3
5
4
5
```

---
**Source:** [https://cses.fi/problemset/task/3429](https://cses.fi/problemset/task/3429)