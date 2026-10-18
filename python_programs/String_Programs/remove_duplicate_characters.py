def remove_duplicate_characters(text):
    return "".join(dict.fromkeys(text))

if __name__ == "__main__":
    print(remove_duplicate_characters("programming"))
