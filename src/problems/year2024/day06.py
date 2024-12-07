import _io
import copy
from typing import Any, Iterable

from src.common.grid import print_grid


def parse_input(fp: _io.FileIO):
    grid = []
    for row in fp.readlines():
        row = row.strip()
        row = list(row)
        grid.append(row)
    return grid


def main(data):
    return level1(mapped_area=copy.deepcopy(data)), level2(
        mapped_area=copy.deepcopy(data)
    )


def level1(mapped_area: list[list[str]]) -> int:
    return len(get_visited_positions(mapped_area=mapped_area))


def level2(mapped_area: list[list[str]]) -> int:
    visited_positions = get_visited_positions(mapped_area=copy.deepcopy(mapped_area))
    guard_position = get_guard_position(mapped_area=mapped_area)

    total_obstructions = 0
    for obstacle_position in visited_positions:
        if obstacle_position == guard_position:
            continue
        if is_a_time_loop(
            mapped_area=copy.deepcopy(mapped_area),
            guard_position=guard_position,
            obstacle_position=obstacle_position,
        ):
            total_obstructions += 1

    return total_obstructions


def get_visited_positions(mapped_area: list[list[str]]) -> set[tuple[int, int]]:
    visited_positions = set()

    guard_position = get_guard_position(mapped_area=mapped_area)
    visited_positions.add(guard_position)
    guard_direction = mapped_area[guard_position[1]][guard_position[0]]
    next_guard_position, is_inside_area = get_next_guard_position(
        guard_position=guard_position,
        guard_direction=guard_direction,
        mapped_area=mapped_area,
    )
    while is_inside_area:
        add_visited_areas(
            visited_positions=visited_positions,
            guard_position=guard_position,
            next_guard_position=next_guard_position,
            guard_direction=guard_direction,
        )
        guard_direction = get_new_guard_direction(guard_direction=guard_direction)

        # Update map
        mapped_area[guard_position[1]][guard_position[0]] = "."
        mapped_area[next_guard_position[1]][next_guard_position[0]] = guard_direction
        # print_grid_with_positions(
        #     grid=mapped_area,
        #     guard_position=next_guard_position,
        #     visited_positions=visited_positions,
        #     guard_direction=guard_direction,
        # )

        guard_position = next_guard_position
        next_guard_position, is_inside_area = get_next_guard_position(
            guard_position=guard_position,
            guard_direction=guard_direction,
            mapped_area=mapped_area,
        )

    # Get last visited positions before the guard exit the area
    add_visited_areas(
        visited_positions=visited_positions,
        guard_position=guard_position,
        next_guard_position=next_guard_position,
        guard_direction=guard_direction,
    )
    return visited_positions


def get_guard_position(mapped_area: list[list[str]]) -> tuple[int, int]:
    for y in range(len(mapped_area)):
        for x in range(len(mapped_area[0])):
            if mapped_area[y][x] in "v<^>":
                return x, y


def get_next_guard_position(
    guard_position: tuple[int, int], guard_direction: str, mapped_area: list[list[str]]
) -> tuple[tuple[int, int], bool]:
    match guard_direction:
        case "^":
            x = guard_position[0]
            for y in range(guard_position[1], -1, -1):
                if mapped_area[y][x] == "#":
                    return (x, y + 1), True
            return (x, 0), False

        case ">":
            y = guard_position[1]
            for x in range(guard_position[0] + 1, len(mapped_area[0])):
                if mapped_area[y][x] == "#":
                    return (x - 1, y), True
            return (len(mapped_area[0]) - 1, y), False

        case "<":
            y = guard_position[1]
            for x in range(guard_position[0] - 1, -1, -1):
                if mapped_area[y][x] == "#":
                    return (x + 1, y), True
            return (0, y), False

        case "v":
            x = guard_position[0]
            for y in range(guard_position[1] + 1, len(mapped_area)):
                if mapped_area[y][x] == "#":
                    return (x, y - 1), True
            return (x, len(mapped_area) - 1), False


def add_visited_areas(
    visited_positions: set[tuple[int, int]],
    guard_position: tuple[int, int],
    next_guard_position: tuple[int, int],
    guard_direction: str,
) -> None:
    match guard_direction:
        case "^":
            for y in range(guard_position[1] - 1, next_guard_position[1] - 1, -1):
                visited_positions.add((guard_position[0], y))
        case ">":
            for x in range(guard_position[0] + 1, next_guard_position[0] + 1):
                visited_positions.add((x, guard_position[1]))
        case "<":
            for x in range(guard_position[0] - 1, next_guard_position[0] - 1, -1):
                visited_positions.add((x, guard_position[1]))
        case "v":
            for y in range(guard_position[1] + 1, next_guard_position[1] + 1):
                visited_positions.add((guard_position[0], y))


def get_new_guard_direction(guard_direction: str) -> str:
    match guard_direction:
        case "^":
            return ">"
        case ">":
            return "v"
        case "<":
            return "^"
        case "v":
            return "<"


def is_a_time_loop(
    mapped_area: list[list[str]],
    obstacle_position: tuple[int, int],
    guard_position: tuple[int, int],
) -> bool:
    # Add obstacle
    mapped_area[obstacle_position[1]][obstacle_position[0]] = "#"

    all_guard_positions = [guard_position]
    guard_direction = mapped_area[guard_position[1]][guard_position[0]]

    next_guard_position, is_inside_area = get_next_guard_position(
        guard_position=guard_position,
        guard_direction=guard_direction,
        mapped_area=mapped_area,
    )
    while is_inside_area:
        guard_direction = get_new_guard_direction(guard_direction=guard_direction)

        # Update map
        mapped_area[guard_position[1]][guard_position[0]] = "."
        mapped_area[next_guard_position[1]][next_guard_position[0]] = guard_direction

        all_guard_positions.append(guard_position)
        guard_position = next_guard_position

        next_guard_position, is_inside_area = get_next_guard_position(
            guard_position=guard_position,
            guard_direction=guard_direction,
            mapped_area=mapped_area,
        )

        if next_guard_position in all_guard_positions:
            return True

    return False


def print_grid_with_positions(
    grid: list[list[Any]],
    visited_positions: Iterable[tuple[int, int]],
    guard_position: tuple[int, int],
    guard_direction: str,
) -> None:
    grid = copy.deepcopy(grid)
    for position in visited_positions:
        grid[position[1]][position[0]] = "X"
    grid[guard_position[1]][guard_position[0]] = guard_direction
    print_grid(grid)
