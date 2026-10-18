def replace_repeated_words(text):
    seen = set()
    result = []
    for word in text.split():
        key = word.casefold()
        result.append("_" if key in seen else word)
        seen.add(key)
    return " ".join(result)

if __name__ == "__main__":
    print(replace_repeated_words("this is a test this is fun"))
