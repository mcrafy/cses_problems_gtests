# Salary Queries

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

A company has n employees with certain salaries. Your task is to keep track of the salaries and process queries.

# Input

The first input line contains two integers n and q: the number of employees and queries. The employees are numbered 1,2,\ldots,n.

The next line has n integers p\_1,p\_2,\ldots,p\_n: each employee's salary.

After this, there are q lines describing the queries. Each line has one of the following forms:

- `!` k x: change the salary of employee k to x
- `?` a b: count the number of employees whose salary is between a \ldots b

# Output

Print the answer to each `?` query.

# Constraints

- 1 ≤ n, q ≤ 2 · 10<sup>5</sup>
- 1 ≤ p\_i ≤ 10<sup>9</sup>
- 1 ≤ k ≤ n
- 1 ≤ x ≤ 10<sup>9</sup>
- 1 ≤ a ≤ b ≤ 10<sup>9</sup>

# Example

Input:

```
5 3
3 7 2 2 5
? 2 3
! 3 6
? 2 3
```

Output:

```
3
2
```

---
**Source:** [https://cses.fi/problemset/task/1144](https://cses.fi/problemset/task/1144)