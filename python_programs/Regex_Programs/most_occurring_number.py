import re
from collections import Counter

def most_occurring_number(text):
    numbers = re.findall(r"\d+", text)
    return Counter(numbers).most_common(1)[0] if numbers else None

if __name__ == "__main__":
    print(most_occurring_number("12 5 12 7 5 12"))
