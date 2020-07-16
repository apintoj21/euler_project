"""Summation of primes
Problem statement:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

from p7 import is_prime


def main():
    prime_2000000 = [x for x in range(2000000) if is_prime(x)]
    sum_prime = sum(list(prime_2000000))
    print(sum_prime)


if __name__ == "__main__":
    main()
