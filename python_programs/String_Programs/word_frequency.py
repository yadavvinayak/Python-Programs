from collections import Counter
import re

def word_frequency(text):
    return Counter(re.findall(r"\b\w+\b", text.casefold()))

if __name__ == "__main__":
    print(word_frequency("Python is fun; Python is useful."))
