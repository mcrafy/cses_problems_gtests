# Visible Buildings Queries

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

There are n buildings in a row numbered 1, 2,…, n from left to right. You are standing to the left of the first building. You can see a building if it is taller than all buildings to its left.

Your task is to process q queries: If only buildings in range [a, b] existed, how many buildings would you see?

# Input

The first line has two integers n and q: the number of buildings and queries.

The second line has n integers h\_1, h\_2, …, h\_n: the heights of the buildings.

Finally, there are q lines describing the queries. Each line has two integers a and b.

# Output

For each query, print one integer: the number of visible buildings.

# Constraints

- 1 ≤ n ≤ 10<sup>5</sup>
- 1 ≤ q ≤ 2 · 10<sup>5</sup>
- 1 ≤ h\_i ≤ 10<sup>9</sup>
- 1 ≤ a ≤ b ≤ n

# Example

Input:

```
5 3
4 1 2 2 3
1 5
2 5
3 4
```

Output:

```
1
3
1
```

---
**Source:** [https://cses.fi/problemset/task/3304](https://cses.fi/problemset/task/3304)