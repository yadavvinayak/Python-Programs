def is_binary_string(text):
    return bool(text) and all(char in "01" for char in text)

if __name__ == "__main__":
    print(is_binary_string("101001"))
