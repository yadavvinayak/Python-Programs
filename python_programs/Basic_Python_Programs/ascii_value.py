if __name__ == "__main__":
    character = input("Enter one character: ")
    if len(character) != 1:
        raise SystemExit("Please enter exactly one character.")
    print("Unicode code point (ASCII for ASCII characters):", ord(character))
