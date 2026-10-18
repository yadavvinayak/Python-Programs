from urllib.parse import urlparse

def is_valid_url(value):
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc) and "." in parsed.netloc

if __name__ == "__main__":
    print(is_valid_url(input("URL: ")))
