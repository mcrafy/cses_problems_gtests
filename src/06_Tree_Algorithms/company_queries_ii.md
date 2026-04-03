# Company Queries Ii

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

A company has n employees, who form a tree hierarchy where each employee has a boss, except for the general director.

Your task is to process q queries of the form: who is the lowest common boss of employees a and b in the hierarchy?

# Input

The first input line has two integers n and q: the number of employees and queries. The employees are numbered 1,2,…,n, and employee 1 is the general director.

The next line has n-1 integers e\_2,e\_3,…,e\_n: for each employee 2,3,…,n their boss.

Finally, there are q lines describing the queries. Each line has two integers a and b: who is the lowest common boss of employees a and b?

# Output

Print the answer for each query.

# Constraints

- 1 ≤ n,q ≤ 2 · 10<sup>5</sup>
- 1 ≤ e\_i ≤ i-1
- 1 ≤ a,b ≤ n

# Example

Input:

```
5 3
1 1 3 3
4 5
2 5
1 4
```

Output:

```
3
1
1
```

---
**Source:** [https://cses.fi/problemset/task/1688](https://cses.fi/problemset/task/1688)