import _io
import itertools
from functools import lru_cache


def parse_input(fp: _io.FileIO):
    equations = []
    for row in fp.readlines():
        row = row.strip()
        test_value, numbers = row.split(":")
        equation = (int(test_value), list(map(int, numbers.strip().split(" "))))
        equations.append(equation)
    return equations


def main(equations: list[tuple[int, list[int]]]):
    return level1(equations=equations), level2(equations=equations)


def level1(equations: list[tuple[int, list[int]]]) -> int:
    return solve_equations(equations=equations, operators="*+")


def level2(equations: list[tuple[int, list[int]]]) -> int:
    return solve_equations(equations=equations, operators="*+|")


def solve_equations(equations: list[tuple[int, list[int]]], operators: str) -> int:
    total = 0
    for equation in equations:
        test_value, numbers = equation
        if is_equation_true(
            test_value=test_value, numbers=numbers, operators=operators
        ):
            total += test_value
    return total


def is_equation_true(test_value: int, numbers: list[int], operators: str) -> bool:
    # Generate all possible combinations of operators
    for combination in itertools.product(operators, repeat=len(numbers) - 1):
        result = numbers[0]
        for idx_number in range(len(numbers) - 1):
            result = compute(
                result, numbers[idx_number + 1], operator=combination[idx_number]
            )
        if result == test_value:
            return True

    return False


@lru_cache
def compute(number_left: int, number_right: int, operator: str) -> int:
    match operator:
        case "*":
            return number_left * number_right
        case "+":
            return number_left + number_right
        case "|":
            return int(str(number_left) + str(number_right))
