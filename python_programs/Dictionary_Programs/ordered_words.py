def ordered_words(words):
    return [word for word in words if "".join(sorted(word)) == word]

if __name__ == "__main__":
    print(ordered_words(["abc", "aab", "xyz", "cat"]))
