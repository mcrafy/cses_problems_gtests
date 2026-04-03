# Range Queries And Copies

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Your task is to maintain a list of arrays which initially has a single array. You have to process the following types of queries:

1. Set the value a in array k to x.
2. Calculate the sum of values in range [a,b] in array k.
3. Create a copy of array k and add it to the end of the list.

# Input

The first input line has two integers n and q: the array size and the number of queries.

The next line has n integers t\_1,t\_2,\ldots,t\_n: the initial contents of the array.

Finally, there are q lines describing the queries. The format of each line is one of the following: "1 k a x", "2 k a b" or "3 k".

# Output

Print the answer to each sum query.

# Constraints

- 1 ≤ n, q ≤ 2 · 10<sup>5</sup>
- 1 ≤ t\_i, x ≤ 10<sup>9</sup>
- 1 ≤ a ≤ b ≤ n

# Example

Input:

```
5 6
2 3 1 2 5
3 1
2 1 1 5
2 2 1 5
1 2 2 5
2 1 1 5
2 2 1 5
```

Output:

```
13
13
13
15
```

---
**Source:** [https://cses.fi/problemset/task/1737](https://cses.fi/problemset/task/1737)