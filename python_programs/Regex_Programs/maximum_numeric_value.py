import re

def maximum_number(text):
    values = [int(value) for value in re.findall(r"\d+", text)]
    return max(values) if values else None

if __name__ == "__main__":
    print(maximum_number("abc 12 and 301 xyz 99"))
