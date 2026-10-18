from collections import Counter

def duplicate_characters(text):
    return {char: count for char, count in Counter(text).items() if count > 1}

if __name__ == "__main__":
    print(duplicate_characters("programming"))
