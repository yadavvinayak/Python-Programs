def can_become_empty(text, pattern):
    if not pattern:
        raise ValueError("pattern cannot be empty")
    while pattern in text:
        text = text.replace(pattern, "", 1)
    return text == ""

if __name__ == "__main__":
    print(can_become_empty("abcabc", "abc"))
