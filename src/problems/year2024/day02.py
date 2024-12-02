import _io

import numpy as np

from src.common.iterators import all_elements_except_one


def parse_input(fp: _io.FileIO):
    reports = []
    for row in fp.readlines():
        row = row.strip()
        reports.append(list(map(int, row.split())))
    return reports


def main(data):
    return (level1(reports=data), level2(reports=data))


def level1(reports: list[list[int]]) -> int:
    return sum(map(report_is_safe, reports))


def level2(reports: list[list[int]]) -> int:
    return sum(map(report_is_safe_dampened, reports))


def report_is_safe(report: list[int]) -> bool:
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    if not (
        all(elem < 0 for elem in differences) or all(elem > 0 for elem in differences)
    ):
        return False

    for elem in np.abs(differences):
        if elem == 0 or elem > 3:
            return False

    return True


def report_is_safe_dampened(report: list[int]) -> bool:
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    is_increasing = differences[0] > 0
    for idx_diff, difference in enumerate(differences):
        if (is_increasing and (difference < 0)) or (
            (not is_increasing) and (difference > 0)
        ):
            return any(map(report_is_safe, all_elements_except_one(report)))

    for idx_diff, difference in enumerate(np.abs(differences)):
        if difference == 0 or difference > 3:
            return any(map(report_is_safe, all_elements_except_one(report)))

    return True
