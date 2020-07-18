"""Lattice paths
Problem statement:

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
from functools import reduce
from time import time as t


def main():
    f1 = lambda num: reduce(lambda x, y: x * y, range(1, num + 1), 1)  # better
    f = lambda n: n - 1 + abs(n - 1) and f(n - 1) * n or 1

    n, m = 20, 20
    # 137846528820
    print(f(5))
    # s1 = t()
    # print("Routes through a", n, "x", m, "grid", f(n + m) // f(n) // f(m))
    # e1 = t()
    # print(e1-s1)
    s2 = t()
    print("Routes through a", n, "x", m, "grid", f1(n + m) // f1(n) // f1(m))
    e2 = t()
    print(e2 - s2)


if __name__ == "__main__":
    main()
