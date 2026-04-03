# Stick Game

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Consider a game where two players remove sticks from a heap. The players move alternately, and the player who removes the last stick wins the game.

A set P=\{p\_1,p\_2,\ldots,p\_k\} determines the allowed moves. For example, if P=\{1,3,4\}, a player may remove 1, 3 or 4 sticks.

Your task is find out for each number of sticks 1,2,…,n if the first player has a winning or losing position.

# Input

The first input line has two integers n and k: the number of sticks and moves.

The next line has k integers p\_1,p\_2,…,p\_k that describe the allowed moves. All integers are distinct, and one of them is 1.

# Output

Print a string containing n characters: `W` means a winning position, and `L` means a losing position.

# Constraints

- 1 ≤ n ≤ 10<sup>6</sup>
- 1 ≤ k ≤ 100
- 1 ≤ p\_i ≤ n

# Example

Input:

```
10 3
1 3 4
```

Output:

```
WLWWWWLWLW
```

---
**Source:** [https://cses.fi/problemset/task/1729](https://cses.fi/problemset/task/1729)