import sys
import time

from src.parse_input import parse_input
from src.problems.year2024.day01_historian_hysteria import historian_hysteria


def main():
    sys.setrecursionlimit(1_000_000)

    problems = {
        1: historian_hysteria,
    }

    for problem_number, problem_function in problems.items():
        t1 = time.time()
        input_data = parse_input(
            path_dir_input="inputs",
            problem_number=problem_number,
        )
        results = problem_function(input_data)
        t2 = time.time()
        print(
            format_problem_results(
                problem_number=problem_number,
                problem_function=problem_function,
                results=results,
                time_to_completion=t2 - t1,
            )
        )


def format_problem_results(
    problem_number: int,
    problem_function: callable,
    results: tuple[int, int],
    time_to_completion: float,
) -> str:
    return f"{problem_number}. {problem_function.__name__} : {', '.join(str(result) for result in results)} ({round(time_to_completion, 4)}s)"


if __name__ == "__main__":
    main()
