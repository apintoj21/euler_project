"""Longest Collatz sequence
Problem statement:

The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz(number):
    yield number
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            yield number
        else:
            number = number * 3 + 1
            yield number


def collatz_len(num):
    count = 1
    while num > 1:
        if num % 2 == 0:
            num = num // 2
            count += 1
        else:
            num = num * 3 + 1
            count += 1
    return count


def longest_chain(limit):
    int1 = 0
    max_chain = -1
    for x in range(1, limit):
        c = collatz_len(x)
        if c > max_chain:
            max_chain = c
            int1 = x
    return int1, max_chain


def main():
    c2= collatz(3)
    l2 = list(c2)
    print(l2)
    print(len(l2))
    c1 = collatz_len(3)
    print(c1)
    intial1, len_max = longest_chain(1000000)
    print(intial1)
    print(len_max)
    c3 = collatz(intial1)
    l3 =list(c3)
    print(l3)
    print(len(l3))



if __name__ == "__main__":
    main()
