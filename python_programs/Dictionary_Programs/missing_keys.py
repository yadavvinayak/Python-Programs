def get_or_default(mapping, key, default=None):
    return mapping.get(key, default)

if __name__ == "__main__":
    print(get_or_default({"a": 1}, "missing", 0))
