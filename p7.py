"""10001st prime
Problem statement:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
from math import sqrt
from itertools import count, islice

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def main():
    prime_10001 = islice((x for x in count() if is_prime(x)),10001)
    p =list(prime_10001)[-1]
    print(p)


if __name__ == "__main__":
    main()
