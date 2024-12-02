from itertools import islice


def batched(iterable: iter, n: int):
    """Batch data into tuples of length n. The last batch may be shorter.
    batched('ABCDEFG', 3) --> ABC DEF G
    """
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def pair_by_pair(iterable: iter) -> tuple[int, int]:
    """Identical to itertools.pairwise"""
    for idx in range(len(iterable) - 1):
        yield iterable[idx], iterable[idx + 1]


def cycle(iterable: iter):
    while True:
        for element in iterable:
            yield element


def all_elements_except_one(iterable: iter):
    for idx in range(len(iterable)):
        yield iterable[:idx] + iterable[idx + 1 :]
