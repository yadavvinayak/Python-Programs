from collections import Counter

def most_frequent_character(text):
    return Counter(text).most_common(1)[0] if text else None

if __name__ == "__main__":
    print(most_frequent_character(input("Text: ")))
