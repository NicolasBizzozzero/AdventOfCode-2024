from typing import Any


def rotate_90_right(grid: list[list[Any]]) -> list[list[Any]]:
    """
    Rotates a 2D grid 90 degrees to the right (clockwise).

    Args:
        grid (list[list[Any]]): A 2D list representing the grid.

    Returns:
        list[list[Any]]: The rotated grid.
    """
    return [list(row) for row in zip(*grid[::-1])]


def rotate_180(grid: list[list[Any]]) -> list[list[Any]]:
    """
    Rotates a 2D grid 180 degrees.

    Args:
        grid (list[list[Any]]): A 2D list representing the grid.

    Returns:
        list[list[Any]]: The rotated grid.
    """
    return [row[::-1] for row in grid[::-1]]


def rotate_90_left(grid: list[list[Any]]) -> list[list[Any]]:
    """
    Rotates a 2D grid 90 degrees to the left (counterclockwise).

    Args:
        grid (list[list[Any]]): A 2D list representing the grid.

    Returns:
        list[list[Any]]: The rotated grid.
    """
    return [list(row) for row in zip(*grid)][::-1]


def transpose(grid: list[list[Any]]) -> list[list[Any]]:
    """
    Transposes a 2D grid (flips it over its diagonal).

    Args:
        grid (list[list[Any]]): A 2D list representing the grid.

    Returns:
        list[list[Any]]: The transposed grid.
    """
    return [list(row) for row in zip(*grid)]
