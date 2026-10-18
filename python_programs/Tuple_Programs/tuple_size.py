import sys

if __name__ == "__main__":
    values = (1, 2, 3, 4)
    print("Length:", len(values))
    print("Approximate object size:", sys.getsizeof(values), "bytes")
