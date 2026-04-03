# Stair Game

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

There is a staircase consisting of n stairs, numbered 1,2,\ldots,n. Initially, each stair has some number of balls.

There are two players who move alternately. On each move, a player chooses a stair k where k ≠ 1 and it has at least one ball. Then, the player moves any number of balls from stair k to stair k-1. The player who moves last wins the game.

Your task is to find out who wins the game when both players play optimally.

Note that if there are no possible moves at all, the second player wins.

# Input

The first input line has an integer t: the number of tests. After this, t test cases are described:

The first line contains an integer n: the number of stairs.

The next line has n integers p\_1,p\_2,\ldots,p\_n: the initial number of balls on each stair.

# Output

For each test, print "first" if the first player wins the game and "second" if the second player wins the game.

# Constraints

- 1 ≤ t ≤ 2 · 10<sup>5</sup>
- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- 0 ≤ p\_i ≤ 10<sup>9</sup>
- the sum of all n is at most 2 · 10<sup>5</sup>

# Example

Input:

```
3
3
0 2 1
4
1 1 1 1
2
5 3
```

Output:

```
first
second
first
```

---
**Source:** [https://cses.fi/problemset/task/1099](https://cses.fi/problemset/task/1099)