import _io

from src.common.iterables import first_index_of_consecutive_items
from src.common.maths import is_even


def parse_input(fp: _io.FileIO):
    return fp.read().strip()


def main(disk_map: str) -> tuple[int, int]:
    return level1(disk_map=disk_map), level2(disk_map=disk_map)


def level1(disk_map: str) -> int:
    blocks = disk_map_to_blocks(disk_map=disk_map)
    defragmented_blocks = block_defragmentation(blocks=blocks)
    checksum = filesystem_checksum(defragmented_blocks=defragmented_blocks)
    return checksum


def level2(disk_map: str) -> int:
    blocks = disk_map_to_blocks(disk_map=disk_map)
    defragmented_blocks = block_defragmentation_whole_files(blocks=blocks)
    checksum = filesystem_checksum(defragmented_blocks=defragmented_blocks)
    return checksum


def disk_map_to_blocks(disk_map: str) -> list[int]:
    blocks = []
    for idx_block, block in enumerate(disk_map):
        if is_even(idx_block):
            blocks += [idx_block // 2] * int(block)
        else:
            blocks += [-1] * int(block)
    return blocks


def block_defragmentation(blocks: list[int]) -> list[int]:
    while -1 in blocks:
        # Remove empty last block
        if blocks[-1] == -1:
            blocks.pop()
        else:
            # Replace first empty block by last block
            idx_empty_block = blocks.index(-1)
            blocks[idx_empty_block] = blocks.pop()
    return blocks


def block_defragmentation_whole_files(blocks: list[int]) -> list[int]:
    max_block_id = blocks[-1]

    for block_id in range(max_block_id, 1, -1):
        idx_block = blocks.index(block_id)
        block_length = blocks.count(block_id)
        idx_empty = first_index_of_consecutive_items(
            iterable=blocks, item=-1, length=block_length
        )
        if idx_empty is None:
            continue
        else:
            if idx_empty <= idx_block:
                for j in range(block_length):
                    blocks[idx_empty + j] = block_id
                    blocks[idx_block + j] = -1
    return blocks


def filesystem_checksum(defragmented_blocks: list[int]) -> int:
    checksum = 0
    for block_idx, block_id in enumerate(defragmented_blocks):
        if block_id != -1:
            checksum += block_idx * block_id
    return checksum
