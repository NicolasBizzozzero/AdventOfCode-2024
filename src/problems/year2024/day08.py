import _io
import itertools

from src.common.grid import is_in_grid


def parse_input(fp: _io.FileIO):
    grid = []
    for row in fp.readlines():
        row = row.strip()
        row = list(row)
        grid.append(row)
    return grid


def main(city: list[list[str]]) -> tuple[int, int]:
    return level1(city=city), level2(city=city)


def level1(city: list[list[str]]) -> int:
    all_frequencies = get_frequencies(city=city)
    all_anti_nodes = set()

    for antenna in all_frequencies.keys():
        frequencies = all_frequencies[antenna]
        for frequency1, frequency2 in itertools.permutations(frequencies, 2):
            anti_node = generate_anti_node(frequency1=frequency1, frequency2=frequency2)
            if is_in_grid(point=anti_node, grid=city):
                all_anti_nodes.add(anti_node)

    return len(all_anti_nodes)


def level2(city: list[list[str]]) -> int:
    all_frequencies = get_frequencies(city=city)
    all_anti_nodes = set()

    for antenna in all_frequencies.keys():
        frequencies = all_frequencies[antenna]
        for frequency1, frequency2 in itertools.permutations(frequencies, 2):
            # frequency2 is always in-line with frequency1
            all_anti_nodes.add(frequency2)

            # Generate a contiguous line of anti_nodes until out of bounds
            anti_node = generate_anti_node(frequency1=frequency1, frequency2=frequency2)
            while is_in_grid(point=anti_node, grid=city):
                all_anti_nodes.add(anti_node)
                anti_node, frequency2 = (
                    generate_anti_node(frequency1=frequency2, frequency2=anti_node),
                    anti_node,
                )

    return len(all_anti_nodes)


def get_frequencies(city: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    frequencies = dict()
    for y in range(len(city)):
        for x in range(len(city[0])):
            antenna = city[y][x]
            if antenna != ".":
                if antenna in frequencies.keys():
                    frequencies[antenna].append((x, y))
                else:
                    frequencies[antenna] = [(x, y)]

    # Remove antenna with only one frequency, they do not produce anti node
    for antenna in frequencies.keys():
        if len(frequencies[antenna]) == 1:
            del frequencies[antenna]

    return frequencies


def generate_anti_node(
    frequency1: tuple[int, int], frequency2: tuple[int, int]
) -> tuple[int, int]:
    x_sym = 2 * frequency2[0] - frequency1[0]
    y_sym = 2 * frequency2[1] - frequency1[1]

    return x_sym, y_sym
