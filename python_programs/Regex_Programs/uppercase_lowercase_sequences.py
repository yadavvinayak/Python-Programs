import re

def upper_lower_sequences(text):
    return re.findall(r"[A-Z]+[a-z]+", text)

if __name__ == "__main__":
    print(upper_lower_sequences("Hello WORLD TestCase"))
