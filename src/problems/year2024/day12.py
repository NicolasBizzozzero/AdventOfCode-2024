import _io


from src.common.grid import iter_grid_idx, grid_iter_adjacent


def parse_input(fp: _io.FileIO):
    grid = []
    for row in fp.readlines():
        row = row.strip()
        row = list(row)
        grid.append(row)

    regions = build_regions(garden=grid)
    return regions


def main(regions: dict[int, set[tuple[int, int]]]) -> tuple[int, int]:
    price = 0
    price_discount = 0

    for region in regions.values():
        price += compute_price(region=region)
        price_discount += compute_price_discount(region=region)
    return price, price_discount


def build_regions(garden: list[list[str]]) -> dict[int, set[tuple[int, int]]]:
    regions = dict()
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
    return regions


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


def region_perimeter(region: set[tuple[int, int]]) -> int:
    """Given a set of (x,y) coordinates which forms a contiguous regions, returns the perimeter of this region.

    :param region: The set of contiguous coordinates
    :return: The perimeter of the region
    """
    # Define the relative positions of the four possible neighbors (top, bottom, left, right)
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Top  # Bottom  # Right  # Left

    perimeter = 0

    for x, y in region:
        # Check each neighbor to determine if it is part of the region
        for dx, dy in neighbors:
            neighbor = (x + dx, y + dy)
            if neighbor not in region:
                # If the neighbor is not in the region, this side contributes to the perimeter
                perimeter += 1

    return perimeter


def region_sides(region: set[tuple[int, int]]) -> int:
    """Given a set of (x,y) coordinates which forms a contiguous regions, returns the number of sides the figure formed
    by those coordinates contains.
    The number of sides == the number of corners of your polygon. So for each point, we just check that a corner exists
    """
    if len(region) == 1:
        return 4

    sides = 0
    for x, y in region:
        # Outer corners
        sides += (x - 1, y) not in region and (x, y - 1) not in region
        sides += (x + 1, y) not in region and (x, y - 1) not in region
        sides += (x - 1, y) not in region and (x, y + 1) not in region
        sides += (x + 1, y) not in region and (x, y + 1) not in region

        # Inner corners
        sides += (
            (x - 1, y) in region
            and (x, y - 1) in region
            and (x - 1, y - 1) not in region
        )
        sides += (
            (x + 1, y) in region
            and (x, y - 1) in region
            and (x + 1, y - 1) not in region
        )
        sides += (
            (x - 1, y) in region
            and (x, y + 1) in region
            and (x - 1, y + 1) not in region
        )
        sides += (
            (x + 1, y) in region
            and (x, y + 1) in region
            and (x + 1, y + 1) not in region
        )

    return sides


def compute_price(region: set[tuple[int, int]]) -> int:
    return region_area(region) * region_perimeter(region)


def compute_price_discount(region: set[tuple[int, int]]) -> int:
    return region_area(region) * region_sides(region)
