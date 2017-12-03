#!/usr/bin/env pypy3
"""Advent of Code 2017: Day 3

--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an
infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern
starting at a location marked 1 and then counting up while
spiraling outward. For example, the first few squares are
allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped),
requested data must be carried back to square 1 (the location of
the only access port for this memory system) by programs that
can only move up, down, left, or right. They always take the
shortest path: the Manhattan Distance between the location of
the data and square 1.

For example:

- Data from square 1 is carried 0 steps, since it's at the
  access port.
- Data from square 12 is carried 3 steps, such as: down, left,
  left.
- Data from square 23 is carried only 2 steps: up twice.
- Data from square 1024 must be carried 31 steps.
- How many steps are required to carry the data from the square
  identified in your puzzle input all the way to the access
  port?

--- Part Two ---
As a stress test on the system, the programs here clear the grid
and then store the value 1 in square 1. Then, in the same
allocation order as shown above, they store the sum of the
values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

- Square 1 starts with the value 1.
- Square 2 has only one adjacent filled square (with value 1),
  so it also stores 1.
- Square 3 has both of the above squares as neighbors and stores
  the sum of their values, 2.
- Square 4 has all three of the aforementioned squares as
  neighbors and stores the sum of their values, 4.
- Square 5 only has the first and fourth squares as neighbors,
  so it gets the value 5.

Once a square is written, its value does not change. Therefore,
the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle
input?
"""
from itertools import cycle, islice
from typing import Any, Iterator

from utils import addv, nth, puzzle_input

ORIGIN = (0, 0)

SW, W, NW, S, N, SE, E, NE = DIRECTIONS = [(i, j)
                                           for i in range(-1, 2)
                                           for j in range(-1, 2) if i or j]

HALVES = cycle([(E, N), (W, S)])


def carry_distance(index: int) -> int:
    """Find the carry distance from a square to the access port.

    >>> carry_distance(1)
    0
    >>> carry_distance(12)
    3
    >>> carry_distance(23)
    2
    >>> carry_distance(1024)
    31
    """
    return manhattan_distance(ORIGIN, nth(spiral(), index - 1))


def stress_test(limit: int) -> int:
    """Sum adj squares and return the first value exceeding the limit.

    >>> stress_test(limit=747)
    806
    """
    s = {}
    for point in spiral():
        s[point] = sum_of_adjacent(s, point)
        if s[point] > limit:
            return s[point]


def sum_of_adjacent(spiral: dict, point: tuple) -> int:
    """Find the sum of squares adjacent to a point in a spiral."""
    if point == ORIGIN:
        return 1

    return sum(spiral.get(n, 0) for n in neighbors(point))


def neighbors(point: Iterator[tuple]) -> Iterator:
    """Yield all points adjacent to a given `point`.

    >>> list(neighbors((0, 0)))
    [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    """
    return (addv(point, direction) for direction in DIRECTIONS)


def manhattan_distance(p1: tuple, p2: tuple):
    """Find the Manhattan distance between two points.

    >>> manhattan_distance((0, 0), (6, 6))
    12
    """
    x, y = p1
    a, b = p2
    return abs(x - a) + abs(y - b)


def spiral():
    """Generate the points of an infinite spiral.

    >>> s = spiral()
    >>> [next(s) for _ in range(5)]
    [(0, 0), (1, 0), (1, 1), (0, 1), (-1, 1)]
    """
    position = (0, 0)

    yield position

    for length, half in enumerate(cycle(HALVES), 1):
        for step in half:
            for _ in range(length):
                position = addv(position, step)
                yield position


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with puzzle_input(3) as f:
        N = int(f.read())

    print(carry_distance(N))  # part 1
    print(stress_test(N))  # part 2
