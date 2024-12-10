def replace_char_at_index(s: str, index: int, new_char: str) -> str:
    """
    Replace the character in a string at a specific index with another character.

    Parameters:
    - s (str): The original string.
    - index (int): The index of the character to replace.
    - new_char (str): The character to replace with.

    Returns:
    - str: The modified string.

    Raises:
    - ValueError: If the index is out of range.
    - ValueError: If new_char is not a single character.
    """
    if not (0 <= index < len(s)):
        raise ValueError("Index is out of range.")
    if len(new_char) != 1:
        raise ValueError("new_char must be a single character.")

    return s[:index] + new_char + s[index + 1 :]
