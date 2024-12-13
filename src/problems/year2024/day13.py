"""All buttons combinations only have one solution, so no need to generate them all"""

import _io
import re
from dataclasses import dataclass

import numpy as np

from src.common.iterators import batched


@dataclass
class Machine:
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]


def parse_input(fp: _io.FileIO):
    machines = []
    for row in batched(fp.readlines(), n=4):
        if len(row) == 4:
            button_a, button_b, price, _ = row
        else:
            button_a, button_b, price = row

        button_a = tuple(map(int, re.findall(r"[+-]?\d+", button_a.strip())))
        button_b = tuple(map(int, re.findall(r"[+-]?\d+", button_b.strip())))
        price = tuple(map(int, re.findall(r"[+-]?\d+", price.strip())))

        machines.append(Machine(button_a, button_b, price))

    return machines


def main(machines: list[Machine]) -> tuple[int, int]:
    return level1(machines=machines), level2(machines=machines)


def level1(machines: list[Machine]) -> int:
    cost = 0
    for machine in machines:
        buttons_combination = find_cheapest_buttons_combination(machine=machine)
        if buttons_combination[0] > 100 or buttons_combination[1] > 100:
            continue
        cost += compute_cost(buttons_combination)
    return cost


def level2(machines: list[Machine], padding: int = 10_000_000_000_000) -> int:
    cost = 0
    for machine in machines:
        machine.prize = (
            machine.prize[0] + padding,
            machine.prize[1] + padding,
        )
        buttons_combination = find_cheapest_buttons_combination(machine=machine)
        if is_claw_on_prize(claw=buttons_combination, machine=machine):
            cost += compute_cost(buttons_combination)
    return cost


def find_cheapest_buttons_combination(machine: Machine) -> tuple[int, int]:
    solution = np.linalg.solve(
        np.array(
            [
                machine.button_a,
                machine.button_b,
            ]
        ).T,
        machine.prize,
    )
    solution = tuple(map(int, solution.round()))
    return solution


def compute_cost(buttons_combination: tuple[int, int]) -> int:
    return 3 * buttons_combination[0] + 1 * buttons_combination[1]


def is_claw_on_prize(claw: tuple[int, int], machine: Machine) -> bool:
    return machine.prize == (
        machine.button_a[0] * claw[0] + machine.button_b[0] * claw[1],
        machine.button_a[1] * claw[0] + machine.button_b[1] * claw[1],
    )


def generate_all_buttons_combinations(
    machine: Machine, max_button_press: int
) -> list[tuple[int, int]]:
    combinations = []
    for a in range(0, max_button_press + 1):
        for b in range(0, max_button_press + 1):
            if is_claw_on_prize(machine=machine, claw=(a, b)):
                combinations.append((a, b))
    return combinations


def get_cheapest_buttons_combination(
    buttons_combinations: list[tuple[int, int]]
) -> tuple[int, int]:
    cheapest_combination = buttons_combinations[0]
    cheapest_cost = compute_cost(cheapest_combination)
    for combination in buttons_combinations[1:]:
        if (cost := compute_cost(combination)) < cheapest_cost:
            cheapest_combination = combination
            cheapest_cost = cost
    return cheapest_combination
