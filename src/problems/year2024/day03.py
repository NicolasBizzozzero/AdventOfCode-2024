import _io

import numpy as np


def parse_input(fp: _io.FileIO):
    for row in fp.readlines():
        print(row)
    exit(0)


def main(data):
    return (
        level1(data=data),
        # level2(data=data)
    )


def level1(data) -> int:
    print(data)
    exit(0)


def level2(data) -> int: ...
