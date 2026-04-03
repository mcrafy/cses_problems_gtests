# Missing Coin Sum Queries

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You have n coins with positive integer values. The coins are numbered 1,2,…,n.

Your task is to process q queries of the form: "if you can use coins a … b, what is the smallest sum you cannot produce?"

# Input

The first input line has two integers n and q: the number of coins and queries.

The second line has n integers x\_1,x\_2,…,x\_n: the value of each coin.

Finally, there are q lines that describe the queries. Each line has two values a and b: you can use coins a … b.

# Output

Print the answer for each query.

# Constraints

- 1 ≤ n, q ≤ 2 · 10<sup>5</sup>
- 1 ≤ x\_i ≤ 10<sup>9</sup>
- 1 ≤ a ≤ b ≤ n

# Example

Input:

```
5 3
2 9 1 2 7
2 4
4 4
1 5
```

Output:

```
4
1
6
```

Explanation: First you can use coins [9,1,2], then coins [2] and finally coins [2,9,1,2,7].

---
**Source:** [https://cses.fi/problemset/task/2184](https://cses.fi/problemset/task/2184)