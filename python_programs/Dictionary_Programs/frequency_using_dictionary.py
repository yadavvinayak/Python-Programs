def frequencies(values):
    result = {}
    for value in values:
        result[value] = result.get(value, 0) + 1
    return result

if __name__ == "__main__":
    print(frequencies(["a", "b", "a", "c", "b", "a"]))
