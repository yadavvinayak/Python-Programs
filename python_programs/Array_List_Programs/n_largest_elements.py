def n_largest(values, n):
    if n < 0:
        raise ValueError("n must be non-negative")
    return sorted(values, reverse=True)[:n]

if __name__ == "__main__":
    print(n_largest([4, 1, 9, 7, 3], 3))
