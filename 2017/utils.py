import os
from contextlib import contextmanager
from itertools import islice
from typing import Any, Iterator


def addv(*vectors):
    """Add up some vectors.

    >>> addv((-1, -1), (1, 1))
    (0, 0)
    """
    return tuple(sum(p) for p in zip(*vectors))


def nth(i: Iterator, n: int) -> Any:
    """Get the nth element from a given iterator.

    >>> nth(range(1, 5), 3)
    4
    """
    return next(islice(i, n, None))


@contextmanager
def puzzle_input(day):
    path = os.path.dirname(__file__)
    day = str(day).rjust(2, '0')
    f = os.path.join(path, f'input/day{day}.txt')
    with open(f, 'r') as f:
        yield f
