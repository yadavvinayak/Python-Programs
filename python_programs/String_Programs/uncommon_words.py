from collections import Counter

def uncommon_words(first, second):
    counts = Counter(first.split()) + Counter(second.split())
    return [word for word, count in counts.items() if count == 1]

if __name__ == "__main__":
    print(uncommon_words("red blue green", "blue yellow"))
