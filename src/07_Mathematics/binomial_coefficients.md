# Binomial Coefficients

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Your task is to calculate n binomial coefficients modulo 10<sup>9</sup>+7.

A binomial coefficient {a \choose b} can be calculated using the formula \frac{a!}{b!(a-b)!}. We assume that a and b are integers and 0 ≤ b ≤ a.

# Input

The first input line contains an integer n: the number of calculations.

After this, there are n lines, each of which contains two integers a and b.

# Output

Print each binomial coefficient modulo 10<sup>9</sup>+7.

# Constraints

- 1 ≤ n ≤ 10<sup>5</sup>
- 0 ≤ b ≤ a ≤ 10<sup>6</sup>

# Example

Input:

```
3
5 3
8 1
9 5
```

Output:

```
10
8
126
```

---
**Source:** [https://cses.fi/problemset/task/1079](https://cses.fi/problemset/task/1079)