def split_and_join(text, separator="-"):
    return separator.join(text.split())

if __name__ == "__main__":
    print(split_and_join("Python string split and join"))
