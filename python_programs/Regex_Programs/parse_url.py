from urllib.parse import urlparse, parse_qs

if __name__ == "__main__":
    url = urlparse(input("URL: "))
    print("Scheme:", url.scheme)
    print("Host:", url.netloc)
    print("Path:", url.path)
    print("Query:", parse_qs(url.query))
