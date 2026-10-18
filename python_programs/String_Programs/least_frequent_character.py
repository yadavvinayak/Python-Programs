from collections import Counter

def least_frequent(text):
    counts = Counter(text)
    return min(counts, key=lambda char: (counts[char], text.index(char))) if text else None

if __name__ == "__main__":
    print(least_frequent("mississippi"))
