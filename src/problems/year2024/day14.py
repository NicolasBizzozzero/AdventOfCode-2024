import _io
import copy
from dataclasses import dataclass
import re
from math import prod
from typing import Any


from src.common.grid import print_grid


@dataclass
class Robot:
    position: tuple[int, int]
    velocity: tuple[int, int]


def parse_input(fp: _io.FileIO):
    robots = []
    for row in fp.readlines():
        row = row.strip()
        match = re.search(r"p=(-?\d+,-?\d+) v=(-?\d+,-?\d+)", row)
        position, velocity = match.group(1), match.group(2)
        robot = Robot(
            position=tuple(map(int, position.split(","))),
            velocity=tuple(map(int, velocity.split(","))),
        )
        robots.append(robot)
    return robots


def main(robots: list[Robot]) -> tuple[int, int]:
    grid_width = 101
    grid_height = 103
    return (
        level1(
            robots=copy.deepcopy(robots), grid_height=grid_height, grid_width=grid_width
        ),
        level2(
            robots=copy.deepcopy(robots), grid_height=grid_height, grid_width=grid_width
        ),
    )


def level1(robots: list[Robot], grid_width: int, grid_height: int) -> int:
    seconds = 100
    for robot in robots:
        robot.position = position_after(
            robot=robot, seconds=seconds, grid_height=grid_height, grid_width=grid_width
        )
    return safety_factor(robots=robots, grid_width=grid_width, grid_height=grid_height)


def level2(robots: list[Robot], grid_width: int, grid_height: int) -> int:
    seconds = 0
    while True:
        seconds += 1
        for robot in robots:
            robot.position = position_after(
                robot=robot,
                seconds=1,
                grid_height=grid_height,
                grid_width=grid_width,
            )
        if is_easter_egg(
            robots=robots,
            grid_height=grid_height,
            grid_width=grid_width,
            pattern="11111111",  # Un miracle que ça fonctionne, mes prières ont été entendues
        ):
            print_grid_robots(
                robots=robots, grid_height=grid_height, grid_width=grid_width
            )
            return seconds


def position_after(
    robot: Robot, seconds: int, grid_width: int, grid_height: int
) -> tuple[int, int]:
    return (
        (robot.position[0] + robot.velocity[0] * seconds) % grid_width,
        (robot.position[1] + robot.velocity[1] * seconds) % grid_height,
    )


def create_grid(width: int, height: int, fill_value: Any) -> list[list[Any]]:
    return [[fill_value for _ in range(width)] for _ in range(height)]


def safety_factor(robots: list[Robot], grid_width: int, grid_height: int) -> int:
    mid_x = grid_width // 2
    mid_y = grid_height // 2
    quadrants = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
    for robot in robots:
        x, y = robot.position

        if x == mid_x or y == mid_y:
            continue

        if x > mid_x and y > mid_y:
            quadrants["Q1"] += 1  # Top-right
        elif x < mid_x and y > mid_y:
            quadrants["Q2"] += 1  # Top-left
        elif x < mid_x and y < mid_y:
            quadrants["Q3"] += 1  # Bottom-left
        elif x > mid_x and y < mid_y:
            quadrants["Q4"] += 1  # Bottom-right

    return prod(quadrants.values())


def print_grid_robots(robots: list[Robot], grid_width: int, grid_height: int) -> None:
    grid = create_grid(width=grid_width, height=grid_height, fill_value=".")
    for robot in robots:
        if grid[robot.position[1]][robot.position[0]] == ".":
            grid[robot.position[1]][robot.position[0]] = "1"
        else:
            grid[robot.position[1]][robot.position[0]] = str(
                int(grid[robot.position[1]][robot.position[0]]) + 1
            )

    print_grid(grid=grid)


def is_easter_egg(
    robots: list[Robot], grid_width: int, grid_height: int, pattern: str
) -> bool:
    grid = create_grid(width=grid_width, height=grid_height, fill_value=".")
    for robot in robots:
        if grid[robot.position[1]][robot.position[0]] == ".":
            grid[robot.position[1]][robot.position[0]] = "1"
        else:
            grid[robot.position[1]][robot.position[0]] = str(
                int(grid[robot.position[1]][robot.position[0]]) + 1
            )

    for row in grid:
        if pattern in "".join(row):
            return True
    return False
