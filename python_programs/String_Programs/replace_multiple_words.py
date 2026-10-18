def replace_words(text, replacements):
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

if __name__ == "__main__":
    print(replace_words("I like cats and cats", {"cats": "dogs"}))
