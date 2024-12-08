import _io


def parse_input(fp: _io.FileIO):
    page_ordering_rules = []
    pages_to_produce = []
    for row in fp.readlines():
        row = row.strip()
        if "|" in row:
            page_ordering_rules.append(tuple(row.split("|")))
        elif row == "":
            continue
        else:
            pages_to_produce.append(row.split(","))
    return (page_ordering_rules, pages_to_produce)


def main(data):
    page_ordering_rules, pages_to_produce = data
    return (
        level1(page_ordering_rules, pages_to_produce),
        level2(page_ordering_rules, pages_to_produce),
    )


def level1(
    page_ordering_rules: list[tuple[str, str]], pages_to_produce: list[list[str]]
) -> int:
    ordering = compute_ordering_dictionary(page_ordering_rules=page_ordering_rules)

    total = 0
    for update in pages_to_produce:
        if update_is_in_order(update=update, ordering=ordering):
            middle_page = update[len(update) // 2]
            total += int(middle_page)

    return total


def level2(
    page_ordering_rules: list[tuple[str, str]], pages_to_produce: list[list[str]]
) -> int:
    ordering = compute_ordering_dictionary(page_ordering_rules=page_ordering_rules)

    total = 0
    for update in pages_to_produce:
        if not update_is_in_order(update=update, ordering=ordering):
            update = order_update(update=update, ordering=ordering)
            middle_page = update[len(update) // 2]
            total += int(middle_page)
    return total


def compute_ordering_dictionary(
    page_ordering_rules: list[tuple[str, str]]
) -> dict[str, list[str]]:
    ordering = dict()
    for page_before, page_after in page_ordering_rules:
        if page_before in ordering:
            ordering[page_before].append(page_after)
        else:
            ordering[page_before] = [page_after]
    return ordering


def update_is_in_order(
    update: list[str],
    ordering: dict[str, list[str]],
) -> bool:
    for page_left, page_right in iter_pages(update=update):
        if page_left not in ordering.keys():
            return False

        if page_right not in ordering[page_left]:
            return False
    return True


def order_update(update: list[str], ordering: dict[str, list[str]]) -> list[str]:
    sorted_update = []
    while len(update) > 0:
        for page_right in update:
            for page_left in update:
                if page_left == page_right:
                    continue

                if page_left not in ordering.keys():
                    continue

                if page_right not in ordering[page_left]:
                    break
            else:
                # page_right is sorted
                sorted_update.insert(0, page_right)
                update.remove(page_right)
    return sorted_update


def iter_pages(update: list[str], reverse: bool = False) -> tuple[str, str]:
    if reverse:
        for page_right in reversed(update):
            for page_left in update:
                if page_left == page_right:
                    break
                yield page_left, page_right
    else:
        for page_left in update:
            for page_right in reversed(update):
                if page_left == page_right:
                    break
                yield page_left, page_right
