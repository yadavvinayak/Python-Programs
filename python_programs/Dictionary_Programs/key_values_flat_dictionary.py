def flatten(keys, values):
    return dict(zip(keys, values))

if __name__ == "__main__":
    print(flatten(["a", "b"], [1, 2]))
