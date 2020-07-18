"""Number letter counts
Problem statement:

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

import inflect

f = inflect.engine()


def number_letter_counts(x, y):
    sums = 0
    for x in range(x, y + 1):
        s = f.number_to_words(x)
        s1 = s.replace(" ", "")
        s2 = s1.replace("-", "")
        print(s2)
        sums += len(s2)
    return sums


def main():
    letter = number_letter_counts(1, 1000)
    print(letter)


if __name__ == "__main__":
    main()
