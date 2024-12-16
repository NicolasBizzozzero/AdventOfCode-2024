import _io
import copy
import heapq
from collections import deque
from functools import lru_cache
from typing import Any

import numpy as np

from src.common.grid import print_grid, find_element, is_coordinate_valid


def parse_input(fp: _io.FileIO):
    grid = []
    for row in fp.readlines():
        row = row.strip()
        row = list(row)
        grid.append(row)
    return grid


def main(maze: list[list[str]]) -> tuple[int, int]:
    return (
        level1(maze=copy.deepcopy(maze)),
        # level2(maze=copy.deepcopy(maze))
    )


def level1(maze: list[list[str]]) -> int:
    start = find_element(grid=maze, element="S")
    end = find_element(grid=maze, element="E")
    maze[start[1]][start[0]] = "."
    maze[end[1]][end[0]] = "."

    best_path = find_best_path(maze=maze, start=start, end=end)
    best_score = score_path(path=best_path)
    print_grid_path(grid=maze, path=best_path)
    print(best_score)
    exit(0)
    return best_score


def level2(data) -> int: ...


def find_best_path(
    maze: list[list[str]], start: tuple[int, int], end: tuple[int, int]
) -> list[tuple[int, int]]:
    priority_queue = [(0, start, [start], (1, 0))]
    visited = set()

    while priority_queue:
        cost, current, path, current_direction = heapq.heappop(priority_queue)

        if current in visited:
            continue
        visited.add(current)

        if current == end:
            return path  # Return the first shortest path found

        x, y = current

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_pos = (x + dx, y + dy)
            new_direction = (dx, dy)
            if (
                is_coordinate_valid(coordinate=next_pos, grid=maze)
                and maze[y][x] == "."
                and next_pos not in visited
            ):
                # Apply a cost if the reindeer is taking a 90° turn
                rotation_cost = 1000 if current_direction != new_direction else 0
                heapq.heappush(
                    priority_queue,
                    (
                        cost + 1 + rotation_cost,
                        next_pos,
                        path + [next_pos],
                        new_direction,
                    ),
                )
    return []


def score_path(path: list[tuple[int, int]]) -> int:
    score = 0
    previous_step = path[0]
    direction = (1, 0)  # Reindeer start facing east

    for step in path[1:]:
        new_direction = (step[0] - previous_step[0], step[1] - previous_step[1])
        if new_direction != direction:
            direction = new_direction
            score += 1_000
        previous_step = step
        score += 1
    return score


def print_grid_path(grid: list[list[str]], path: list[tuple[int, int]]) -> None:
    grid = copy.deepcopy(grid)

    previous_coord = path[0]

    for coord in path[1:-1]:
        direction = (coord[0] - previous_coord[0], coord[1] - previous_coord[1])
        match direction:
            case (1, 0):
                character = ">"
            case (-1, 0):
                character = "<"
            case (0, 1):
                character = "v"
            case (0, -1):
                character = "^"
        grid[coord[1]][coord[0]] = character
        previous_coord = coord

    grid[path[0][1]][path[0][0]] = "S"
    grid[path[-1][1]][path[-1][0]] = "E"

    print_grid(grid=grid)
