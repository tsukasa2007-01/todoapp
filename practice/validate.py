def is_valid_title(title: str) -> bool:
    trimmed = title.strip()
    if len(trimmed) == 0:
        return False
    if len(trimmed) > 100:
        return False
    return len(trimmed) <= 100


print(is_valid_title("牛乳を買う"))
print(is_valid_title(""))
print(is_valid_title("   "))
print(is_valid_title("あ" * 101))
print(is_valid_title("あ" * 100))


def validate_title(raw_title: str) -> str:
    trimmed = raw_title.strip()
    if len(trimmed) == 0:
        raise ValueError("タイトルは必須です")
    if len(trimmed) > 100:
        raise ValueError("100文字を超えています")
    return trimmed
