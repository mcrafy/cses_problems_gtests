# Company Queries I

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

A company has n employees, who form a tree hierarchy where each employee has a boss, except for the general director.

Your task is to process q queries of the form: who is employee x's boss k levels higher up in the hierarchy?

# Input

The first input line has two integers n and q: the number of employees and queries. The employees are numbered 1,2,…,n, and employee 1 is the general director.

The next line has n-1 integers e\_2,e\_3,…,e\_n: for each employee 2,3,…,n their boss.

Finally, there are q lines describing the queries. Each line has two integers x and k: who is employee x's boss k levels higher up?

# Output

Print the answer for each query. If such a boss does not exist, print -1.

# Constraints

- 1 ≤ n,q ≤ 2 · 10<sup>5</sup>
- 1 ≤ e\_i ≤ i-1
- 1 ≤ x ≤ n
- 1 ≤ k ≤ n

# Example

Input:

```
5 3
1 1 3 3
4 1
4 2
4 3
```

Output:

```
3
1
-1
```

---
**Source:** [https://cses.fi/problemset/task/1687](https://cses.fi/problemset/task/1687)