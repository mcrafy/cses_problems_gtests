# List Removals

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given a list consisting of n integers. Your task is to remove elements from the list at given positions, and report the removed elements.

# Input

The first input line has an integer n: the initial size of the list. During the process, the elements are numbered 1,2,…,k where k is the current size of the list.

The second line has n integers x\_1,x\_2,…,x\_n: the contents of the list.

The last line has n integers p\_1,p\_2,…,p\_n: the positions of the elements to be removed.

# Output

Print the elements in the order they are removed.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ x\_i ≤ 10<sup>9</sup>
- 1 ≤ p\_i ≤ n-i+1

# Example

Input:

```
5
2 6 1 4 2
3 1 3 1 1
```

Output:

```
1 2 2 6 4
```

Explanation: The contents of the list are [2,6,1,4,2], [2,6,4,2], [6,4,2], [6,4], [4] and [].

---
**Source:** [https://cses.fi/problemset/task/1749](https://cses.fi/problemset/task/1749)