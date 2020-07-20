"""Factorial digit sum
Problem statement:

n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""
from functools import reduce
fact = lambda num: reduce(lambda x, y: x * y, range(1, num + 1), 1)

def main():
    f1 = fact(100)
    l1 = list(str(f1))
    sum1 = 0
    for i in l1:
        sum1 += int(i)
    print(sum1)

if __name__ == "__main__":
    main()