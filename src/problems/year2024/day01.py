import _io
from collections import Counter

import numpy as np


def parse_input(fp: _io.FileIO):
    left_list, right_list = [], []
    for row in fp.readlines():
        left_elem, right_elem = row.strip().split()
        left_list.append(int(left_elem))
        right_list.append(int(right_elem))
    return left_list, right_list


def main(data):
    left_list, right_list = data

    return (
        distance_between_lists(left_list=left_list, right_list=right_list),
        similarity_score(left_list=left_list, right_list=right_list),
    )


def distance_between_lists(left_list: list[int], right_list: list[int]) -> int:
    # Sort both lists once
    left_list.sort()
    right_list.sort()

    # Find distance betweens two list
    distances = abs(np.array(left_list) - np.array(right_list))

    # Sum them
    return distances.sum()


def similarity_score(left_list: list[int], right_list: list[int]) -> int:
    right_list = Counter(right_list)

    total = 0
    for number in left_list:
        total += right_list.get(number, 0) * number

    return total
