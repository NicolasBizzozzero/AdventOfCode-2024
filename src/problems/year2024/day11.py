import _io
from collections import defaultdict
from copy import copy

from src.common.maths import is_even


def parse_input(fp: _io.FileIO):
    stones = list(map(int, fp.read().strip().split(" ")))

    # Convert stones to a dictionary mapping their count
    stones_dict = defaultdict(int)
    for stone in stones:
        stones_dict[stone] += 1

    return stones_dict


def main(stones: dict[int, int]) -> tuple[int, int]:
    return (
        count_stones_after_n_blinks(stones=stones, nb_blinks=25),
        count_stones_after_n_blinks(stones=stones, nb_blinks=75),
    )


def count_stones_after_n_blinks(stones: dict[int, int], nb_blinks: int) -> int:
    stones = copy(stones)

    for idx_blink in range(1, nb_blinks + 1):
        blink(stones=stones)

    return sum(stones.values())


def blink(stones: dict[int, int]) -> None:
    for stone, nb_of_stones in copy(stones).items():
        if nb_of_stones != 0:
            blink_at_stone(stone=stone, nb_of_stones=nb_of_stones, stones=stones)


def blink_at_stone(stone: int, nb_of_stones: int, stones: dict[int, int]) -> None:
    stone_str = str(stone)

    if stone == 0:
        stones[1] += nb_of_stones
    elif is_even(len(stone_str)):
        stone_left = int(stone_str[: int(len(stone_str) // 2)])
        stone_right = int(stone_str[int(len(stone_str) // 2) :])
        stones[stone_left] += nb_of_stones
        stones[stone_right] += nb_of_stones
    else:
        stones[stone * 2024] += nb_of_stones

    stones[stone] -= nb_of_stones
