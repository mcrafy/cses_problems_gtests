# Nearest Shops

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

There are n cities and m roads. Each road is bidirectional and connects two cities. It is also known that k cities have an anime shop.

If you live in a city, you of course know the local anime shop well if there is one. You would like to find the nearest anime shop that is not in your city.

For each city, determine the minimum distance to another city that has an anime shop.

# Input

The first line has three integers n, m and k: the number of cities, roads and anime shops. The cities are numbered 1,2,…,n.

The next line contains k integers: the cities that have an anime shop.

Finally, there are m lines that describe the roads. Each line has two integers a and b: there is a road between cities a and b.

# Output

Print n integers: for each city, the minimum distance to another city with an anime shop. If there is no such city, print -1 instead.

# Constraints

- 1 ≤ k ≤ n ≤ 10<sup>5</sup>
- 0 ≤ m ≤ 2 · 10<sup>5</sup>

# Example

Input:

```
9 6 4
2 4 5 7
1 2
1 3
1 8
2 4
3 4
5 6
```

Output:

```
1 1 1 1 -1 1 -1 2 -1
```

---
**Source:** [https://cses.fi/problemset/task/3303](https://cses.fi/problemset/task/3303)