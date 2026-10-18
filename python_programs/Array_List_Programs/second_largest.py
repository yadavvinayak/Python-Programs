def second_largest(values):
    unique = sorted(set(values))
    if len(unique) < 2:
        raise ValueError("need at least two distinct values")
    return unique[-2]

if __name__ == "__main__":
    print(second_largest([4, 1, 9, 9, 7]))
