# Game Routes

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

A game has n levels, connected by m teleporters, and your task is to get from level 1 to level n. The game has been designed so that there are no directed cycles in the underlying graph. In how many ways can you complete the game?

# Input

The first input line has two integers n and m: the number of levels and teleporters. The levels are numbered 1,2,…,n.

After this, there are m lines describing the teleporters. Each line has two integers a and b: there is a teleporter from level a to level b.

# Output

Print one integer: the number of ways you can complete the game. Since the result may be large, print it modulo 10<sup>9</sup>+7.

# Constraints

- 1 ≤ n ≤ 10<sup>5</sup>
- 1 ≤ m ≤ 2 · 10<sup>5</sup>
- 1 ≤ a,b ≤ n

# Example

Input:

```
4 5
1 2
2 4
1 3
3 4
1 4
```

Output:

```
3
```

---
**Source:** [https://cses.fi/problemset/task/1681](https://cses.fi/problemset/task/1681)