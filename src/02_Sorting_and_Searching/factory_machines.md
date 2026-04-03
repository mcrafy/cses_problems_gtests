# Factory Machines

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

A factory has n machines which can be used to make products. Your goal is to make a total of t products.

For each machine, you know the number of seconds it needs to make a single product. The machines can work simultaneously, and you can freely decide their schedule.

What is the shortest time needed to make t products?

# Input

The first input line has two integers n and t: the number of machines and products.

The next line has n integers k\_1,k\_2,…,k\_n: the time needed to make a product using each machine.

# Output

Print one integer: the minimum time needed to make t products.

# Constraints

- 1 ≤ n ≤ 2 · 10<sup>5</sup>
- 1 ≤ t ≤ 10<sup>9</sup>
- 1 ≤ k\_i ≤ 10<sup>9</sup>

# Example

Input:

```
3 7
3 2 5
```

Output:

```
8
```

Explanation: Machine 1 makes two products, machine 2 makes four products and machine 3 makes one product.

---
**Source:** [https://cses.fi/problemset/task/1620](https://cses.fi/problemset/task/1620)