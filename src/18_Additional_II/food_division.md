# Food Division

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

There are n children around a round table. For each child, you know the amount of food they currently have and the amount of food they want. The total amount of food in the table is correct.

At each step, a child can give one unit of food to his or her neighbour. What is the minimum number of steps needed?

# Input

The first input line contains an integer n: the number of children.

The next line has n integers a\_1,a\_2,\ldots,a\_n: the current amount of food for each child.

The last line has n integers b\_1,b\_2,\ldots,b\_n: the required amount of food for each child.

# Output

Print one integer: the minimum number of steps.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- 0 ≤ a\_i, b\_i ≤ 10<sup>6</sup>

# Example

Input:

```
3
3 5 0
2 4 2
```

Output:

```
2
```

*Explanation*: Child 1 gives one unit of food to child 3, and child 2 gives one unit of food to child 3.

---
**Source:** [https://cses.fi/problemset/task/1189](https://cses.fi/problemset/task/1189)