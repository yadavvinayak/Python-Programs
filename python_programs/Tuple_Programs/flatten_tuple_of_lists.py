def flatten(items):
    return tuple(value for group in items for value in group)

if __name__ == "__main__":
    print(flatten(([1, 2], [3], [4, 5])))
