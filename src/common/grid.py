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


def print_grid(grid: list[list[Any]]) -> None:
    for row in grid:
        print("".join(row))
    print()


def get_column(x: int, grid: list[list[Any]]) -> list[Any]:
    """Returns the specified column (x) from the grid."""
    return [row[x] for row in grid]


def get_row(y: int, grid: list[list[Any]]) -> list[Any]:
    """Returns the specified row (y) from the grid."""
    return grid[y]


def is_in_grid(point: tuple[int, int], grid: list[list[str]]) -> bool:
    if not grid or not grid[0]:
        return False

    # Check if the point is within bounds
    return 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0])
