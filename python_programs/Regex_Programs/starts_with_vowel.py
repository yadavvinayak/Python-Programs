import re

def starts_with_vowel(text):
    return re.match(r"^[aeiou]", text, re.IGNORECASE) is not None

if __name__ == "__main__":
    print(starts_with_vowel(input("Text: ")))
