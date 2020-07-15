"""Largest prime factor
Problem statement:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt


def prime_factors(number):
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number /= 2

    for i in range(3, int(sqrt(number)) + 1, 2):
        while number % i == 0:
            factors.append(i)
            number /= i

    if number > 2:
        factors.append(int(number))
    return factors


def main():
    f = prime_factors(600851475143)
    print(f[-1])


if __name__ == "__main__":
    main()
