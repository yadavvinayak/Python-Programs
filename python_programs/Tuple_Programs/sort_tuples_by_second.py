if __name__ == "__main__":
    values = [("a", 3), ("b", 1), ("c", 2)]
    print(sorted(values, key=lambda item: item[1]))
