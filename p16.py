"""Power digit sum
Problem statement:

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

"""
from math import pow


def main():
    x = pow(2,1000)
    l1 = list(str(int(x)))
    print(l1)
    sum = 0
    for i in l1:
        sum += int(i)
    print(sum)

if __name__ == "__main__":
    main()
