"""Smallest multiple
Problem statement:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from p3 import prime_factors


def factors():
    d = {}
    numbers = list(range(1, 21))[::-1]
    for num in numbers:
        m = prime_factors(num)
        for i in set(m):
            if i in d.keys():
                if d[i] < m.count(i):
                    d[i] = m.count(i)
            else:
                d[i] = m.count(i)
    return d


def main():
    sums, fact = 1, factors()
    print(fact)
    for x in fact.keys():
        pw = fact[x]
        sums *= x ** pw

    print(sums)


if __name__ == "__main__":
    main()
