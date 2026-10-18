def unique_values(mapping):
    result = []
    seen = set()
    for value in mapping.values():
        marker = repr(value)
        if marker not in seen:
            seen.add(marker)
            result.append(value)
    return result

if __name__ == "__main__":
    print(unique_values({"a": 1, "b": 2, "c": 1}))
