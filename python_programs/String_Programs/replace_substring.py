def replace_all(text, old, new):
    if old == "":
        raise ValueError("old substring cannot be empty")
    return text.replace(old, new)

if __name__ == "__main__":
    print(replace_all("one fish two fish", "fish", "cat"))
