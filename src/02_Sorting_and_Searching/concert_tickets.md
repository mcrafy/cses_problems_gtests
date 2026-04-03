# Concert Tickets

- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

There are n concert tickets available, each with a certain price. Then, m customers arrive, one after another.

Each customer announces the maximum price they are willing to pay for a ticket, and after this, they will get a ticket with the nearest possible price such that it does not exceed the maximum price.

# Input

The first input line contains integers n and m: the number of tickets and the number of customers.

The next line contains n integers h\_1,h\_2,\ldots,h\_n: the price of each ticket.

The last line contains m integers t\_1,t\_2,\ldots,t\_m: the maximum price for each customer in the order they arrive.

# Output

Print, for each customer, the price that they will pay for their ticket. After this, the ticket cannot be purchased again.

If a customer cannot get any ticket, print -1.

# Constraints

- 1 ≤ n, m ≤ 2 · 10<sup>5</sup>
- 1 ≤ h\_i, t\_i ≤ 10<sup>9</sup>

# Example

Input:

```
5 3
5 3 7 8 5
4 8 3
```

Output:

```
3
8
-1
```

---
**Source:** [https://cses.fi/problemset/task/1091](https://cses.fi/problemset/task/1091)