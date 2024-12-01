import os
import re

from src.common.iterators import batched


def get_path_input(path_dir_input: str, problem_number: int):
    return os.path.join(path_dir_input, f"{problem_number}.txt")


def parse_input(path_dir_input: str, problem_number: int):
    path_input = get_path_input(
        path_dir_input=path_dir_input, problem_number=problem_number
    )

    with open(path_input) as fp:
        match problem_number:
            case 1:
                left_list, right_list = [], []
                for row in fp.readlines():
                    left_elem, right_elem = row.strip().split()
                    left_list.append(int(left_elem))
                    right_list.append(int(right_elem))
                return left_list, right_list

            case _:
                return [line.strip() for line in fp.readlines()]
