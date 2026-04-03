# Permutation Prime Sums

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Given n, create two permutations a and b of size n such that a\_i+b\_i is prime for i=1,2,…,n.

# Input

The only line has an integer n.

# Output

Print two permutations. You can print any valid solution. If there are no solutions, print `IMPOSSIBLE`.

# Constraints

- 1 ≤ n ≤ 10<sup>5</sup>

# Example

Input:

```
5
```

Output:

```
2 1 3 5 4
5 1 4 2 3
```

*Explanation*: The sums are 2+5=7, 1+1=2, 3+4=7, 5+2=7 and 4+3=7 which all are primes.

---
**Source:** [https://cses.fi/problemset/task/3423](https://cses.fi/problemset/task/3423)