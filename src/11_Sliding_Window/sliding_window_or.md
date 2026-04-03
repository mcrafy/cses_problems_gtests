# Sliding Window Or

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

You are given an array of n integers. Your task is to calculate the bitwise or of each window of k elements, from left to right.

In this problem the input data is large and it is created using a generator.

# Input

The first line contains two integers n and k: the number of elements and the size of the window.

The next line contains four integers x, a, b and c: the input generator parameters. The input is generated as follows:

- x\_1=x
- x\_i=(ax\_{i-1}+b) \bmod c for i=2,3,…,n

# Output

Print the xor of all window ors.

# Constraints

- 1 ≤ k ≤ n ≤ 10<sup>7</sup>
- 0 ≤ x, a, b ≤ 10<sup>9</sup>
- 1 ≤ c ≤ 10<sup>9</sup>

# Example

Input:

```
8 5
3 7 1 11
```

Output:

```
4
```

Explanation: The input array is [3,0,1,8,2,4,7,6]. The windows are [3,0,1,8,2], [0,1,8,2,4], [1,8,2,4,7] and [8,2,4,7,6], and their ors are 11, 15, 15 and 15. Thus, the answer is 11 \oplus 15 \oplus 15 \oplus 15 = 4.

---
**Source:** [https://cses.fi/problemset/task/3405](https://cses.fi/problemset/task/3405)