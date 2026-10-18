def remove_duplicate_words(text):
    seen, result = set(), []
    for word in text.split():
        key = word.casefold()
        if key not in seen:
            seen.add(key)
            result.append(word)
    return " ".join(result)

if __name__ == "__main__":
    print(remove_duplicate_words("one two one three Two"))
