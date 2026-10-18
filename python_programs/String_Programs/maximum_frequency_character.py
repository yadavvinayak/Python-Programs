from collections import Counter

def most_frequent(text):
    if not text:
        return None, 0
    char, count = Counter(text).most_common(1)[0]
    return char, count

if __name__ == "__main__":
    print(most_frequent("banana"))
