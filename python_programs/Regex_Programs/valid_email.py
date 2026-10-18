import re

EMAIL = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")

def is_valid_email(value):
    return EMAIL.fullmatch(value) is not None

if __name__ == "__main__":
    print(is_valid_email(input("Email: ")))
