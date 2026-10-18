def without_key(mapping, key):
    result = mapping.copy()
    result.pop(key, None)
    return result

if __name__ == "__main__":
    print(without_key({"a": 1, "b": 2}, "a"))
