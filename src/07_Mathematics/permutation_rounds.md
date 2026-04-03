# Permutation Rounds

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

There is a sorted array [1,2,…,n] and a permutation p\_1,p\_2,…,p\_n. On each round, all elements move according to the permutation: the element at position i moves to position p\_i.

After how many rounds is the array sorted again for the first time?

# Input

The first line has an integer n.

The next line contains n integers p\_1,p\_2,…,p\_n.

# Output

Print the number of rounds modulo 10<sup>9</sup>+7.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>

# Example

Input:

```
8
5 3 2 6 4 1 8 7
```

Output:

```
4
```

*Explanation*: The array changes as follows after the rounds:

- Round 1: [6,3,2,5,1,4,8,7]
- Round 2: [4,2,3,1,6,5,7,8]
- Round 3: [5,3,2,6,4,1,8,7]
- Round 4: [1,2,3,4,5,6,7,8]

---
**Source:** [https://cses.fi/problemset/task/3398](https://cses.fi/problemset/task/3398)