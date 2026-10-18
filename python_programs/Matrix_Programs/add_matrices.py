def add_matrices(a, b):
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise ValueError("matrices must have equal dimensions")
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]

if __name__ == "__main__":
    print(add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
