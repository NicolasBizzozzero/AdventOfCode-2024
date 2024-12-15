""" Assumes that all `yearYYYY` problems are sorted in order and execute them one by one. """

import os
import sys
import time

from src.aoc_utils import (
    get_path_input,
    format_problem_results,
    save_input,
    submit_answer,
)
from src.common.dates import get_current_problem_number
from src.common.meta import load_module

sys.setrecursionlimit(1_000_000)

with open(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "AOC_TOKEN_SESSION.txt")
) as fp:
    os.environ["AOC_TOKEN_SESSION"] = fp.read()


def main(year: str):
    current_problem_number = get_current_problem_number()
    # current_problem_number = 12

    if current_problem_number is None:
        for problem_number in range(1, 25):
            problem_number = str(problem_number).zfill(2)
            execute_problem(year=year, problem_number=problem_number, send_answer=False)
    else:
        execute_problem(
            year=year, problem_number=current_problem_number, send_answer=True
        )


def execute_problem(year: str, problem_number: str, send_answer: bool):
    path_file_input = get_path_input(
        path_dir_input=os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "inputs"
        ),
        problem_number=problem_number,
        year=year,
    )
    if not os.path.exists(path_file_input):
        os.makedirs(os.path.join("inputs", year), exist_ok=True)
        save_input(year=year, day=problem_number, path_file_output=path_file_input)

    module = load_module(
        module_path=os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "src",
            "problems",
            f"year{year}",
            f"day{problem_number}.py",
        )
    )

    t1 = time.time()
    with open(path_file_input, newline="\n") as fp:
        data = module.parse_input(fp=fp)
    results = module.main(data)
    t2 = time.time()

    print(
        format_problem_results(
            problem_number=problem_number,
            results=results,
            time_to_completion=t2 - t1,
        )
    )

    if send_answer:
        if len(results) == 1:
            submit_answer(year=year, day=problem_number, level=1, answer=results[0])
        elif len(results) == 2:
            submit_answer(year=year, day=problem_number, level=2, answer=results[1])
        else:
            raise ValueError(
                f"Impossible to determine level of answer with those results : {results}"
            )


if __name__ == "__main__":
    main(year="2024")
