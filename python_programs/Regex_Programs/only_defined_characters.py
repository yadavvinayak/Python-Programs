import re

def contains_only(text, allowed_pattern=r"[A-Za-z0-9]+"):
    return re.fullmatch(allowed_pattern, text) is not None

if __name__ == "__main__":
    print(contains_only(input("Text: ")))
