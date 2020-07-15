"""Largest palindrome product
Problem statement:

A palindromic number reads the same both ways. The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def reverse(num):
    rev_num = 0
    while num > 0:
        rem = num % 10
        rev_num = (rev_num * 10) + rem
        num = num // 10
    return rev_num


def palindrome_list():
    palindromes =[]
    for x in range(1,1000):
        for y in range(1,1000):
            if x*y == reverse(x*y):
                palindromes.append(x*y)
    return palindromes


def main():
    p = palindrome_list()
    print(max(p))


if __name__ == "__main__":
    main()
