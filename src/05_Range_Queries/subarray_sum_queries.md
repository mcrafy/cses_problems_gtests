# Subarray Sum Queries

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

There is an array consisting of n integers. Some values of the array will be updated, and after each update, your task is to report the maximum subarray sum in the array.

# Input

The first input line contains integers n and m: the size of the array and the number of updates. The array is indexed 1,2,\ldots,n.

The next line has n integers: x\_1,x\_2,\ldots,x\_n: the initial contents of the array.

Then there are m lines describing the changes. Each line has two integers k and x: the value at position k becomes x.

# Output

After each update, print the maximum subarray sum. Empty subarrays (with sum 0) are allowed.

# Constraints

- 1 ≤ n, m ≤ 2 · 10<sup>5</sup>
- -10<sup>9</sup> ≤ x\_i ≤ 10<sup>9</sup>
- 1 ≤ k ≤ n
- -10<sup>9</sup> ≤ x ≤ 10<sup>9</sup>

# Example

Input:

```
5 3
1 2 -3 5 -1
2 6
3 1
2 -2
```

Output:

```
9
13
6
```

---
**Source:** [https://cses.fi/problemset/task/1190](https://cses.fi/problemset/task/1190)