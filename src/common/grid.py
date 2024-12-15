from typing import Any, Iterable, Generator


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


def grid_index(grid: list[list[Any]], element: Any) -> list[tuple[int, int]]:
    """
    Finds all occurrences of an element in a 2D grid and returns their indices.

    Args:
        grid (List[List[Any]]): A 2D list representing the grid.
        element (Any): The element to search for.

    Returns:
        List[Tuple[int, int]]: A list of tuples where each tuple is a pair of row and column indices of the element.
    """
    indices = []
    for row_idx, row in enumerate(grid):
        for col_idx, value in enumerate(row):
            if value == element:
                indices.append((col_idx, row_idx))
    return indices


def grid_is_value_adjacent(
    grid: list[list[Any]], idx: tuple[int, int], value_adjacent: Any
) -> bool:
    """
    Checks if a given value is adjacent to a specified index in a 2D grid.

    Args:
        grid (List[List[Any]]): A 2D list representing the grid.
        idx (Tuple[int, int]): A tuple containing the row and column index to check around.
        value_adjacent (Any): The value to check for adjacency.

    Returns:
        bool: True if the value is adjacent to the given index, False otherwise.
    """
    row, col = idx
    rows, cols = len(grid), len(grid[0])

    # Define the relative directions for adjacency: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        adj_row, adj_col = row + dr, col + dc

        # Check if the adjacent cell is within bounds
        if 0 <= adj_row < rows and 0 <= adj_col < cols:
            if grid[adj_row][adj_col] == value_adjacent:
                return True

    return False


def grid_iter_adjacent(
    grid: list[list[Any]], idx: tuple[int, int]
) -> Iterable[tuple[int, int]]:
    """
    Iterates over all valid adjacent cells of a given index in a 2D grid.

    Args:
        grid (List[List[Any]]): A 2D list representing the grid.
        idx (Tuple[int, int]): A tuple containing the row and column index to check around.
    """
    # Define the relative directions for adjacency: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for direction in directions:
        idx_adjacent = (idx[0] + direction[0], idx[1] + direction[1])
        if is_in_bound(grid=grid, idx=idx_adjacent):
            yield idx_adjacent


def is_in_bound(grid: list[list[Any]], idx: tuple[int, int]) -> bool:
    """
    Checks if a given index is within the bounds of a 2D grid.

    Args:
        grid (List[List[Any]]): A 2D list representing the grid.
        idx (Tuple[int, int]): A tuple containing the row and column index to check.

    Returns:
        bool: True if the index is within the bounds of the grid, False otherwise.
    """
    row, col = idx
    rows, cols = len(grid), len(grid[0])
    return 0 <= row < rows and 0 <= col < cols


def iter_grid(grid: list[list[Any]]) -> Iterable[Any]:
    """
    Iterates through each element in a 2D grid.

    Args:
        grid (list[list[Any]]): A 2D list to iterate over.

    Yields:
        Any: Each element of the grid.
    """
    for row in grid:
        for element in row:
            yield element


def iter_grid_idx(grid: list[list[Any]]) -> Iterable[tuple[int, int]]:
    """
    Iterates through each element in a 2D grid, yielding its indices and value.

    Args:
        grid (list[list[Any]]): A 2D list to iterate over.

    Yields:
        Tuple[int, int]: A tuple containing the row index, column index, and the value at that position.
    """
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            yield x, y


def is_grid_mirrored(grid: list[list[Any]]) -> bool:
    if not grid:
        return True  # An empty grid is considered symmetrical.

    for row in grid:
        if row != row[::-1]:
            return False

    return True
