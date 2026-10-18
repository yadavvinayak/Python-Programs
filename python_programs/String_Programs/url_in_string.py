import re

URL_PATTERN = re.compile(r"https?://[^\s]+", re.IGNORECASE)

def find_urls(text):
    return URL_PATTERN.findall(text)

if __name__ == "__main__":
    print(find_urls("Visit https://example.com for details."))
