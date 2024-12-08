import _io
from typing import Any

from src.common.grid import rotate_90_right


# TODO: Make iterators


def parse_input(fp: _io.FileIO):
    grid = []
    for row in fp.readlines():
        row = row.strip()
        row = list(row)
        grid.append(row)
    return grid


def main(grid):
    return level1(grid=grid), level2(grid=grid)


def level1(grid) -> int:
    word = "XMAS"

    total = 0
    total += word_count_horizontal_left_to_right(grid, word)
    total += word_count_diagonal_top_left_to_bottom_right(grid, word)
    grid = rotate_90_right(grid)
    total += word_count_horizontal_left_to_right(grid, word)
    total += word_count_diagonal_top_left_to_bottom_right(grid, word)
    grid = rotate_90_right(grid)
    total += word_count_horizontal_left_to_right(grid, word)
    total += word_count_diagonal_top_left_to_bottom_right(grid, word)
    grid = rotate_90_right(grid)
    total += word_count_horizontal_left_to_right(grid, word)
    total += word_count_diagonal_top_left_to_bottom_right(grid, word)

    return total


def level2(grid) -> int:
    total = 0
    total += xmas_count(grid=grid)
    grid = rotate_90_right(grid)
    total += xmas_count(grid=grid)
    grid = rotate_90_right(grid)
    total += xmas_count(grid=grid)
    grid = rotate_90_right(grid)
    total += xmas_count(grid=grid)
    return total


def word_count_horizontal_left_to_right(grid: list[list[Any]], word: str) -> int:
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0]) - len(word) + 1):
            for idx_char, char in enumerate(word):
                if grid[y][x + idx_char] != char:
                    break
            else:
                count += 1
    return count


def word_count_diagonal_top_left_to_bottom_right(
    grid: list[list[Any]], word: str
) -> int:
    count = 0
    for y in range(len(grid) - len(word) + 1):
        for x in range(len(grid[0]) - len(word) + 1):
            for idx_char, char in enumerate(word):
                if grid[y + idx_char][x + idx_char] != char:
                    break
            else:
                count += 1
    return count


def xmas_count(grid: list[list[Any]]) -> int:
    count = 0
    for y in range(len(grid) - 2):
        for x in range(len(grid[0]) - 2):
            if (
                grid[y][x] == "M"
                and grid[y + 1][x + 1] == "A"
                and grid[y + 2][x] == "M"
                and grid[y][x + 2] == "S"
                and grid[y + 2][x + 2] == "S"
            ):
                count += 1
    return count
