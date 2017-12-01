#!/usr/bin/env python3
"""Advent of Code 2017: Day 1

You're standing in a room with "digitization quarantine" written
in LEDs along one wall. The only door is locked, but it includes
a small interface.  "Restricted Area - Strictly No Digitized
Users Allowed."

It goes on to explain that you may only leave by solving a
captcha to prove you're not a human. Apparently, you only get
one millisecond to solve the captcha: too fast for a normal
human, but it feels like hours to you.

The captcha requires you to review a sequence of digits (your
puzzle input) and find the sum of all digits that match the next
digit in the list. The list is circular, so the digit after the
last digit is the first digit in the list.

For example:

  - 1122 produces a sum of 3 (1 + 2) because the first digit (1)
    matches the second digit and the third digit (2) matches the
    fourth digit.
  - 1111 produces 4 because each digit (all 1) matches the next.
  - 1234 produces 0 because no digit matches the next.
  - 91212129 produces 9 because the only digit that matches the
    next one is the last digit, 9.

What is the solution to your captcha?
"""

import os
from typing import Iterable, Iterator


def chunk(l: Iterable) -> Iterator:
    """Associate each item with its nearest neighbor to the right (wrapping).

    Example:
      >>> list(chunk('123'))
      [('1', '2'), ('2', '3'), ('3', '1')]
    """
    c = len(l)
    return ((l[i], l[(i + 1) % c]) for i in range(c))


def solve(digits: Iterable) -> int:
    """Solve the CAPTCHA.

    >>> solve('1122')
    3
    >>> solve('1111')
    4
    >>> solve('1234')
    0
    >>> solve('91212129')
    9
    """
    return sum(int(a) for a, b in chunk(digits) if a == b)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    path = os.path.dirname(__file__)
    with open(os.path.join(path, 'day01.txt')) as f:
        digits = f.read().strip()
        print(solve(digits))
