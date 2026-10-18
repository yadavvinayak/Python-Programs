def digits_from_numbers(items):
    return tuple(int(char) for item in items for char in str(abs(item)) if char.isdigit())

if __name__ == "__main__":
    print(digits_from_numbers((123, 45, 6)))
