import _io
import re


def parse_input(fp: _io.FileIO):
    result = ""
    for row in fp.readlines():
        row = row.strip()
        result += row
    return result.strip()


def main(memory: str):
    return (level1(memory=memory), level2(memory=memory))


def level1(memory: str) -> int:
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)
    result = 0
    for x, y in matches:
        result += int(x) * int(y)
    return result


def level2(memory: str) -> int:
    matches = re.findall(r"(don't)\(\)|(do)\(\)|mul\((\d{1,3}),(\d{1,3})\)", memory)
    result = 0
    instructions_enabled = True

    for dont, do, x, y in matches:
        if do != "":
            instructions_enabled = True
        if dont != "":
            instructions_enabled = False
        if instructions_enabled and x != "" and y != "":
            result += int(x) * int(y)

    return result
