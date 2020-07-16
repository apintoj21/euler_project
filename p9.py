"""Special Pythagorean triplet
Problem statement:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def main():
    for a in range(3, 500):
        for b in range(a + 1, 499):
            cr2 = a ** 2 + b ** 2
            c = cr2 ** 0.5

            if a + b + c == 1000:
                product = a * b * c
                d = a ** 2 + b ** 2
                e = c ** 2
                print(f"{a},{b},{int(c)}")
                print(d)
                print(int(e))
                print(int(product))
                break


if __name__ == "__main__":
    main()
