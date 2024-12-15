import _io
import copy

import numpy as np


def parse_input(fp: _io.FileIO):
    for row in fp.readlines():
        row = row.strip()
        print(row)
    exit(0)


def main(data) -> tuple[int, int]:
    return (
        level1(data=copy.deepcopy(data)),
        # level2(data=copy.deepcopy(data))
    )


def level1(data) -> int:
    print(data)
    exit(0)


def level2(data) -> int: ...
