# Lines And Queries Ii

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Your task is to efficiently process the following types of queries:

1. Add a line ax+b that is active in range [l,r]
2. Find the maximum point in any active line at position x

# Input

The first line has an integer n: the number of queries.

The following n lines describe the queries. The format of each line is either "1 a b l r" or "2 x".

# Output

Print the answer for each query of type 2. If no line is active, print `NO`.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- -10<sup>9</sup> ≤ a,b ≤ 10<sup>9</sup>
- 0 ≤ x ≤ 10<sup>5</sup>
- 0 ≤ l ≤ r ≤ 10<sup>5</sup>

# Example

Input:

```
6
1 1 2 1 3
2 3
2 4
1 0 4 1 5
2 3
2 4
```

Output:

```
5
NO
5
4
```

---
**Source:** [https://cses.fi/problemset/task/3430](https://cses.fi/problemset/task/3430)