# Finding Patterns

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Given a string and patterns, check for each pattern if it appears in the string.

# Input

The first input line has a string of length n.

The next input line has an integer k: the number of patterns. Finally, there are k lines that describe the patterns.

The string and the patterns consist of characters a–z.

# Output

For each pattern, print "YES" if it appears in the string and "NO" otherwise.

# Constraints

- 1 ≤ n ≤ 10<sup>5</sup>
- 1 ≤ k ≤ 5 · 10<sup>5</sup>
- the total length of the patterns is at most 5 · 10<sup>5</sup>

# Example

Input:

```
aybabtu
3
bab
abc
ayba
```

Output:

```
YES
NO
YES
```

---
**Source:** [https://cses.fi/problemset/task/2102](https://cses.fi/problemset/task/2102)