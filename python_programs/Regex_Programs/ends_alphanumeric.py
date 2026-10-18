import re

def ends_alphanumeric(text):
    return re.search(r"[A-Za-z0-9]$", text) is not None

if __name__ == "__main__":
    print(ends_alphanumeric("example1"))
