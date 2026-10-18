import re

def strength(password):
    score = sum([
        len(password) >= 12,
        bool(re.search(r"[a-z]", password)),
        bool(re.search(r"[A-Z]", password)),
        bool(re.search(r"\d", password)),
        bool(re.search(r"[^A-Za-z0-9]", password))
    ])
    return "Strong" if score >= 4 and len(password) >= 12 else "Weak"

if __name__ == "__main__":
    print(strength(input("Password: ")))
