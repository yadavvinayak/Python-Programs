def character_types(text):
    return {
        "uppercase": sum(char.isupper() for char in text),
        "lowercase": sum(char.islower() for char in text),
        "digits": sum(char.isdigit() for char in text),
        "spaces": sum(char.isspace() for char in text),
        "other": sum(not (char.isalnum() or char.isspace()) for char in text)
    }

if __name__ == "__main__":
    print(character_types(input("Text: ")))
