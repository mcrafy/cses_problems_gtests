# Subarray Sum Constraints

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Your task is to construct an array x\_1,x\_2,…,x\_n consisting of n integers.

The array must satisfy m constraints of the form (l,r,s): the sum x\_l + x\_{l+1} + … + x\_r must equal s.

# Input

The first line has two integers n and m: the length of the array and the number of constraints.

The next m lines each have three integers l, r and s: the description of the constraints.

# Output

If a solution exists, print `YES` on the first line.

On the second line, print n integers x\_1, x\_2,…, x\_n: the contents of the array. All elements of the array must satisfy -10^{15} ≤ x\_i ≤ 10^{15} and the array must satisfy all given constraints. You can print any valid solution.

If no solution exists, just print `NO`.

# Constraints

- 1 ≤ n ≤ 5000
- 0 ≤ m ≤ 2 · 10<sup>5</sup>
- 1 ≤ l ≤ r ≤ n
- -10<sup>9</sup> ≤ s ≤ 10<sup>9</sup>

# Example

Input:

```
5 3
1 3 3
3 5 3
4 4 -1
```

Output:

```
YES
0 2 1 -1 3
```

---
**Source:** [https://cses.fi/problemset/task/3294](https://cses.fi/problemset/task/3294)