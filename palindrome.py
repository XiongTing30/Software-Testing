def is_palindrome(text: str) -> bool:
    """检查字符串是否为回文，如 aba, level"""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
