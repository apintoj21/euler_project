"""Highly divisible triangular number
Problem statement:

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""
from itertools import count, islice
from functools import reduce

triangle_num_1000 = islice((int(x * (x + 1) / 2) for x in count(1)), 1000)


def factors(num):
    return set(reduce(list.__add__, ([div, num // div] for div in range(1, int(num ** 0.5) + 1) if num % div == 0)))


def triangle_factors_greaterthan(limit):
    for x in count(1):
        tri_num = int(x * (x + 1) / 2)
        f = factors(tri_num)
        if len(f) > limit:
            print(tri_num)
            break


def main():
    l1 = list(triangle_num_1000)
    print(l1)
    f = factors(12)
    print(len(f))
    triangle_factors_greaterthan(500)


if __name__ == "__main__":
    main()
