import re

def add_spaces(text):
    return re.sub(r"(?<!^)(?=[A-Z])", " ", text)

if __name__ == "__main__":
    print(add_spaces("ThisIsPython"))
