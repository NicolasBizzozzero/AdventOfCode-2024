from collections import Counter

import numpy as np


def historian_hysteria(lists: tuple[list[int], list[int]]):
    left_list, right_list = lists
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
