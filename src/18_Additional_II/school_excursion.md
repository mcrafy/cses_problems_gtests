# School Excursion

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

A group of n children are coming to Helsinki. There are two possible attractions: a child can visit either Korkeasaari (zoo) or Linnanmäki (amusement park).

There are m pairs of children who want to visit the same attraction. Your task is to find all possible alternatives for the number of children that will visit Korkeasaari. The children's wishes have to be taken into account.

# Input

The first input line has two integers n and m: the number of children and their wishes. The children are numbered 1,2,…,n.

After this, there are m lines describing the children's wishes. Each line has two integers a and b: children a and b want to visit the same attraction.

# Output

Print a bit string of length n where a one-bit at index i indicates that it is possible that exactly i children visit Korkeasaari (the bit string is to be considered one-indexed).

# Constraints

- 1 ≤ n ≤ 10<sup>5</sup>
- 0 ≤ m ≤ 10<sup>5</sup>
- 1 ≤ a,b ≤ n

# Example

Input:

```
5 3
1 2
2 3
1 5
```

Output:

```
10011
```

*Explanation*: The number of children visiting Korkeasaari can be 1, 4 or 5.

---
**Source:** [https://cses.fi/problemset/task/1706](https://cses.fi/problemset/task/1706)