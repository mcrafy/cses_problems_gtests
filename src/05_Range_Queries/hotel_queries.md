# Hotel Queries

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

There are n hotels on a street. For each hotel you know the number of free rooms. Your task is to assign hotel rooms for groups of tourists. All members of a group want to stay in the same hotel.

The groups will come to you one after another, and you know for each group the number of rooms it requires. You always assign a group to the first hotel having enough rooms. After this, the number of free rooms in the hotel decreases.

# Input

The first input line contains two integers n and m: the number of hotels and the number of groups. The hotels are numbered 1,2,\ldots,n.

The next line contains n integers h\_1,h\_2,\ldots,h\_n: the number of free rooms in each hotel.

The last line contains m integers r\_1,r\_2,\ldots,r\_m: the number of rooms each group requires.

# Output

Print the assigned hotel for each group. If a group cannot be assigned a hotel, print 0 instead.

# Constraints

- 1 ≤ n,m ≤ 2 · 10<sup>5</sup>
- 1 ≤ h\_i ≤ 10<sup>9</sup>
- 1 ≤ r\_i ≤ 10<sup>9</sup>

# Example

Input:

```
8 5
3 2 4 1 5 5 2 6
4 4 7 1 1
```

Output:

```
3 5 0 1 1
```

---
**Source:** [https://cses.fi/problemset/task/1143](https://cses.fi/problemset/task/1143)