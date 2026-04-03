# Coding Company

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Your company has n coders, and each of them has a skill level between 0 and 100. Your task is to divide the coders into teams that work together.

Based on your experience, you know that teams work well when the skill levels of the coders are about the same. For this reason, the penalty for creating a team is the skill level difference between the best and the worst coder.

In how many ways can you divide the coders into teams such that the sum of the penalties is at most x?

# Input

The first input line has two integers n and x: the number of coders and the maximum allowed penalty sum.

The next line has n integers t\_1,t\_2,…,t\_n: the skill level of each coder.

# Output

Print one integer: the number of valid divisions modulo 10<sup>9</sup>+7.

# Constraints

- 1 ≤ n ≤ 100
- 0 ≤ x ≤ 5000
- 0 ≤ t\_i ≤ 100

# Example

Input:

```
3 2
2 5 3
```

Output:

```
3
```

---
**Source:** [https://cses.fi/problemset/task/1665](https://cses.fi/problemset/task/1665)