import datetime


def get_current_problem_number() -> str | None:
    current_time = datetime.datetime.now()

    # If we are outside AoC dates, returns all problems
    if current_time.month != 12 or current_time.day < 1 or current_time.day > 25:
        return None

    if current_time.hour >= 6:
        problem_number = current_time.day
    else:
        problem_number = (current_time - datetime.timedelta(days=1)).day

    return str(problem_number).zfill(2)
