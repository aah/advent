import os
from contextlib import contextmanager


@contextmanager
def puzzle_input(day):
    path = os.path.dirname(__file__)
    day = str(day).rjust(2, '0')
    f = os.path.join(path, f'day{day}.txt')
    with open(f, 'r') as f:
        yield f
