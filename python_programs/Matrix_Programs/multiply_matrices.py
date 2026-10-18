def multiply_matrices(a, b):
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("incompatible matrix dimensions")
    if any(len(row) != len(a[0]) for row in a) or any(len(row) != len(b[0]) for row in b):
        raise ValueError("matrices must be rectangular")
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

if __name__ == "__main__":
    print(multiply_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
