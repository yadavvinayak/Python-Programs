from collections import Counter

def possible_words(characters, words):
    available = Counter(characters.casefold())
    return [word for word in words if not (Counter(word.casefold()) - available)]

if __name__ == "__main__":
    print(possible_words("act", ["cat", "act", "tac", "dog"]))
