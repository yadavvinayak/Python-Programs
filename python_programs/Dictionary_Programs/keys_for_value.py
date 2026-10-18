def keys_for_value(mapping, target):
    return [key for key, value in mapping.items() if value == target]

if __name__ == "__main__":
    print(keys_for_value({"a": 1, "b": 2, "c": 1}, 1))
