# Bubble Sort Rounds Ii

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Bubble sort is a sorting algorithm that consists of a number of rounds. On each round the algorithm scans the array from left to right and swaps any adjacent elements that are in the wrong order.

Given an array of n integers, find out the contents of the array after k bubble sort rounds.

# Input

The first line has two integers n and k: the array size and the number of rounds.

The next line has n integers x\_1,x\_2,…,x\_n: the array contents.

# Output

Print n integers: the contents of the array after k rounds.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- 0 ≤ k ≤ 10<sup>9</sup>
- 1 ≤ x\_i ≤ 10<sup>9</sup>

# Example

Input:

```
5 2
3 2 4 1 4
```

Output:

```
2 1 3 4 4
```

---
**Source:** [https://cses.fi/problemset/task/3152](https://cses.fi/problemset/task/3152)