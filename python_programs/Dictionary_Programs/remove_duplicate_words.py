def remove_duplicate_words(sentence):
    return " ".join(dict.fromkeys(sentence.split()))

if __name__ == "__main__":
    print(remove_duplicate_words("red blue red green blue"))
