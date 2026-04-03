# Maximum Average Subarrays

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given an array of n integers. For each i = 1, 2,…, n, your task is to find the subarray ending at index i with the largest average. If there are multiple subarrays with the largest average, you should find the longest one.

# Input

The first line has an integer n: the size of the array.

The next line has n integers x\_1, x\_2,…, x\_n: the contents of the array.

# Output

Print n integers: the length of the subarray ending at index i with the largest average for each i = 1, 2,…, n.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ x\_i ≤ 10<sup>6</sup>

# Example

Input:

```
7
1 6 4 6 2 5 5
```

Output:

```
1 1 2 1 4 1 2
```

*Explanation*: Consider i = 5. The averages of all subarrays ending at index 5 are \frac{1 + 6 + 4 + 6 + 2}{5} = 3.8, \frac{6 + 4 + 6 + 2}{4} = 4.5, \frac{4 + 6 + 2}{3} = 4, \frac{6 + 2}{2} = 4 and \frac{2}{1} = 2. The largest average is 4.5 and the length of the corresponding subarray is 4.

---
**Source:** [https://cses.fi/problemset/task/3301](https://cses.fi/problemset/task/3301)