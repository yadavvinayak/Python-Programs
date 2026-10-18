import re

def password_is_valid(password):
    return (len(password) >= 8 and re.search(r"[A-Z]", password)
            and re.search(r"[a-z]", password) and re.search(r"\d", password))

if __name__ == "__main__":
    print(password_is_valid(input("Password: ")))
