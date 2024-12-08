import os

import requests


class AdventOfCodeConnector:
    url: str = "https://adventofcode.com/{year}/day/{day}"

    def __init__(self, token_session: str):
        self.token_session = token_session

    def get_input(self, year: str, day: str) -> str:
        url = f"{self.url.format(year=year, day=int(day))}/input"

        response = requests.get(
            url, headers={"Cookie": f"session={self.token_session}"}
        )

        match response.status_code:
            case 200:
                return response.text
            case _:
                print(
                    f"Error HTTP {response.status_code}: {response.reason}, {response.text}"
                )
                exit(1)

    def submit_answer(self, year: str, day: str, level: str, answer: str):
        assert str(level) in ("1", "2"), "Level must be only two values, 1 or 2"

        url = f"{self.url.format(year=year, day=int(day))}/answer"
        response = requests.post(
            url,
            data={"level": level, "answer": answer},
            headers={"Cookie": f"session={self.token_session}"},
        )

        if response.status_code != 200:
            print(
                f"Error HTTP {response.status_code}: {response.reason}, {response.text}"
            )
        elif "You don't seem to be solving the right level." in response.text:
            print("Level already solved, cannot submit answer")
        elif "That's the right answer!" in response.text:
            if "[Continue to Part Two]" in response.text:
                print("Successfully answered level 1 !")
            else:
                print("Successfully answered level 2 !")
        elif "That's not the right answer" in response.text:
            if "your answer is too low" in response.text:
                print("Wrong answer, your answer is too low")
            else:
                print("Wrong answer, your answer is too high")
        elif "You gave an answer too recently" in response.text:
            print(
                f"You gave an answer too recently, please wait 1 min between each answers"
            )
        else:
            print(f"Error while submitting answer : {response.text}")


def get_path_input(path_dir_input: str, problem_number: str, year: str):
    return os.path.abspath(os.path.join(path_dir_input, year, f"{problem_number}.txt"))


def format_problem_results(
    problem_number: str,
    results: tuple[int, int],
    time_to_completion: float,
) -> str:
    return f"Day {problem_number} : {', '.join(str(result) for result in results)} ({round(time_to_completion, 4)}s)"


def save_input(year: str, day: str, path_file_output: str):
    connector = AdventOfCodeConnector(token_session=os.environ["AOC_TOKEN_SESSION"])
    result = connector.get_input(year=year, day=day)

    with open(path_file_output, "w", newline="\n") as fp:
        fp.write(result)


def submit_answer(year: str, day: str, level: int, answer: int):
    connector = AdventOfCodeConnector(token_session=os.environ["AOC_TOKEN_SESSION"])
    connector.submit_answer(year=year, day=day, level=str(level), answer=str(answer))
