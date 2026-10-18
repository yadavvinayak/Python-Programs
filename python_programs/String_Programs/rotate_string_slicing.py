def rotate_left(text, steps):
    if not text:
        return text
    steps %= len(text)
    return text[steps:] + text[:steps]

if __name__ == "__main__":
    print(rotate_left("python", 2))
