import _io

from src.common.grid import grid_index, grid_iter_adjacent


def parse_input(fp: _io.FileIO):
    grid = []
    for row in fp.readlines():
        row = row.strip()
        row = list(row)

        # map(int, row) but ignore "."
        for idx in range(len(row)):
            if row[idx] == ".":
                continue
            row[idx] = int(row[idx])

        grid.append(row)
    return grid


def main(topographic_map: list[list[int]]) -> tuple[int, int]:
    return (
        level1(topographic_map=topographic_map),
        level2(topographic_map=topographic_map),
    )


def level1(topographic_map: list[list[int]]) -> int:
    all_idx_stop = grid_index(grid=topographic_map, element=9)

    total = 0
    for trailhead in grid_index(grid=topographic_map, element=0):
        total += compute_trailhead_score(
            topographic_map=topographic_map,
            trailhead=trailhead,
            all_idx_stop=all_idx_stop,
        )

    return total


def level2(topographic_map: list[list[int]]) -> int:
    all_idx_stop = grid_index(grid=topographic_map, element=9)

    total = 0
    for trailhead in grid_index(grid=topographic_map, element=0):
        total += compute_trailhead_rating(
            topographic_map=topographic_map,
            trailhead=trailhead,
            all_idx_stop=all_idx_stop,
        )

    return total


def compute_trailhead_score(
    topographic_map: list[list[int]],
    trailhead: tuple[int, int],
    all_idx_stop: list[tuple[int, int]],
) -> int:
    score = 0
    for idx_stop in all_idx_stop:
        if (
            compute_rating_for_one_trailhead(
                trailhead=trailhead, idx_stop=idx_stop, topographic_map=topographic_map
            )
            >= 1
        ):
            score += 1
    return score


def compute_trailhead_rating(
    topographic_map: list[list[int]],
    trailhead: tuple[int, int],
    all_idx_stop: list[tuple[int, int]],
) -> int:
    rating = 0
    for idx_stop in all_idx_stop:
        rating += compute_rating_for_one_trailhead(
            trailhead=trailhead, idx_stop=idx_stop, topographic_map=topographic_map
        )
    return rating


def compute_rating_for_one_trailhead(
    trailhead: tuple[int, int],
    idx_stop: tuple[int, int],
    topographic_map: list[list[int]],
    current_pos: tuple[int, int] = None,
) -> int:
    # Start of recursion
    if current_pos is None:
        current_pos = trailhead
    current_value = topographic_map[current_pos[1]][current_pos[0]]

    # End of recursion
    if (current_value == 8) and idx_stop in grid_iter_adjacent(
        grid=topographic_map, idx=current_pos
    ):
        return 1

    rating = 0
    for idx_adjacent in grid_iter_adjacent(grid=topographic_map, idx=current_pos):
        value_adjacent = topographic_map[idx_adjacent[1]][idx_adjacent[0]]
        if value_adjacent == current_value + 1:
            rating += compute_rating_for_one_trailhead(
                trailhead=trailhead,
                idx_stop=idx_stop,
                topographic_map=topographic_map,
                current_pos=idx_adjacent,
            )
    return rating
