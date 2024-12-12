import _io

import numpy as np

from src.common.grid import print_grid, iter_grid, iter_grid_idx, grid_iter_adjacent

"""
Je veux construire un dico de regions :
j'itere sur chaque plante :
 - Si elle est dans une region existant, on annule
 - Sinon, on l'ajoute dans une nouvelle region, puis on appelle un algo de constru de region
"""


def parse_input(fp: _io.FileIO):
    grid = []
    for row in fp.readlines():
        row = row.strip()
        row = list(row)
        grid.append(row)
    return grid


def main(garden: list[list[str]]) -> tuple[int, int]:
    return (
        level1(garden=garden),
        # level2(garden=garden)
    )


def level1(garden: list[list[str]]) -> int:
    regions: dict[int, set[tuple[int, int]]] = dict()
    print_grid(garden)

    current_region = 0
    for x, y in iter_grid_idx(grid=garden):
        plot = garden[y][x]
        plot_idx = (x, y)

        # Check if plot has been saved in a region already
        if is_plot_in_built_regions(plot_idx=plot_idx, regions=regions):
            continue

        # Build new region
        build_region(
            plot=plot,
            plot_idx=plot_idx,
            current_region=current_region,
            garden=garden,
            regions=regions,
        )
        current_region += 1

    for region_name in regions.keys():
        region = regions[region_name]
        print(region_name)
        print(region)
        print(region_area(region))
        print(region_perimeter(region))
        print()
    exit(0)


def level2(garden: list[list[str]]) -> int: ...


def build_region(
    plot: str,
    plot_idx: tuple[int, int],
    current_region: int,
    garden: list[list[str]],
    regions: dict[int, set[tuple[int, int]]],
) -> None:
    if not current_region in regions:
        regions[current_region] = set()

    regions[current_region].add(plot_idx)

    for adjacent_idx in grid_iter_adjacent(grid=garden, idx=plot_idx):
        adjacent_plot = garden[adjacent_idx[1]][adjacent_idx[0]]
        if adjacent_plot == plot and not is_plot_in_built_regions(
            plot_idx=adjacent_idx, regions=regions
        ):
            build_region(
                plot=plot,
                plot_idx=adjacent_idx,
                current_region=current_region,
                garden=garden,
                regions=regions,
            )


def is_plot_in_built_regions(
    plot_idx: tuple[int, int], regions: dict[int, set[tuple[int, int]]]
) -> bool:
    return any(plot_idx in values for values in regions.values())


def region_area(region: set[tuple[int, int]]) -> int:
    return len(region)


def region_perimeter(region: set[tuple[int, int]]) -> int: ...
