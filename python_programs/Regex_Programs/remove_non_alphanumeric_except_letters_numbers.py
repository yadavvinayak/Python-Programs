import re

def keep_letters_numbers(text):
    return re.sub(r"[^A-Za-z0-9]", "", text)

if __name__ == "__main__":
    print(keep_letters_numbers("Hello, Python 3.12!"))
