def merge(first, second):
    return {**first, **second}

if __name__ == "__main__":
    print(merge({"a": 1}, {"b": 2, "a": 3}))
