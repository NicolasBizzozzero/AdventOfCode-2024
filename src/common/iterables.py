from typing import Any


def first_index_of_consecutive_items(
    iterable: list[Any], item: Any, length: int
) -> int | None:
    for i in range(len(iterable) - length + 1):
        if iterable[i : i + length] == [item] * length:
            return i
    return None
