# Grid Path Construction

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

Given an n × m grid and two squares a=(y\_1,x\_1) and b=(y\_2,x\_2), create a path from a to b that visits each square exactly once.

For example, here is a path from a=(1,3) to b=(3,6) in a 4 × 7 grid:
![](/file/944079e41a17eca6debb54a7d4da8f9124232206a1d80256432e8a2715c00055)

# Input

The first input line has an integer t: the number of tests.

After this, there are t lines that describe the tests. Each line has six integers n, m, y\_1, x\_1, y\_2 and x\_2.

In all tests 1 ≤ y\_1,y\_2 ≤ n and 1 ≤ x\_1,x\_2 ≤ m. In addition, y\_1 ≠ y\_2 or x\_1 ≠ x\_2.

# Output

Print YES, if it is possible to construct a path, and NO otherwise.

If there is a path, also print its description which consists of characters `U` (up), `D` (down), `L` (left) and `R` (right). If there are several paths, you can print any of them.

# Constraints

- 1 ≤ t ≤ 100
- 1 ≤ n ≤ 50
- 1 ≤ m ≤ 50

# Example

Input:

```
5
1 3 1 1 1 3
1 3 1 2 1 3
2 2 1 1 2 2
2 2 1 1 2 1
4 7 1 3 3 6
```

Output:

```
YES
RR
NO
NO
YES
RDL
YES
RRRRDDDLLLLLLUUURDDRURDRURD
```

---
**Source:** [https://cses.fi/problemset/task/2418](https://cses.fi/problemset/task/2418)