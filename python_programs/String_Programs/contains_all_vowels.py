def contains_all_vowels(text):
    return set("aeiou").issubset(set(text.casefold()))

if __name__ == "__main__":
    print(contains_all_vowels("Education is about a unique idea"))
