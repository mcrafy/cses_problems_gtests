# Minimum Cost Pairs

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Given an array of n integers, consider pairings of k pairs. Each number can appear in at most one pair, and the cost of a pair (a,b) is |a-b|. The cost of a pairing is the sum of all costs of the pairs.

Calculate the minimum costs of pairings for k=1,2,…,\lfloor n/2 \rfloor.

# Input

The first line has an integer: the array size.

The next line has n integers x\_1,x\_2,…,x\_n: the array contents.

# Output

Print \lfloor n/2 \rfloor integers: the minimum costs of pairings.

# Constraints

- 2 ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ x\_i ≤ 10<sup>9</sup>

# Example

Input:

```
8
3 1 2 7 9 3 4 7
```

Output:

```
0 0 1 6
```

*Explanation*: Possible minimum-cost pairings are [(3,3)], [(3,3),(7,7)], [(1,2),(3,3),(7,7)] and [(1,2),(3,3),(4,7),(7,9)].

---
**Source:** [https://cses.fi/problemset/task/3402](https://cses.fi/problemset/task/3402)