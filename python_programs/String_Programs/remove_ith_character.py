def remove_character(text, index):
    if not 0 <= index < len(text):
        raise IndexError("index out of range")
    return text[:index] + text[index + 1:]

if __name__ == "__main__":
    print(remove_character("python", 2))
