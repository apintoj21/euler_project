"""Sum square difference
Problem statement:

The sum of the squares of the first ten natural numbers is,
1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2=55^2=3025
Hence the difference between the sum of the squares of the first ten natural numbers and
the square of the sum is 3025−385=2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_of_square(limit):
    sums = 0
    for x in range(1, limit + 1):
        sums += x * x
    print(sums)
    return sums


def square_of_sum(limit):
    sums = 0
    for x in range(1, limit + 1):
        sums += x
    square = sums ** 2
    print(square)
    return square


def main():
    print(square_of_sum(100) - sum_of_square(100))


if __name__ == "__main__":
    main()
