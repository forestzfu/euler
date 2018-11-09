#!/usr/bin/env python3


def palindrome(num):
    s = str(num)
    return s == s[::-1]


def three_digit():
    curr = 0
    cx, cy = None, None
    for x in reversed(range(100, 1000)):
        for y in reversed(range(100, 1000)):
            p = x * y
            if palindrome(p):
                print(f"{x} * {y} = {p} [{curr}]")
                if p > curr:
                    curr = p
                    cx, cy = x, y

    return curr


if __name__ == '__main__':
    print(three_digit())
