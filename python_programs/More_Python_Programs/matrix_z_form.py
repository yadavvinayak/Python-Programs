def z_form(matrix):
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be non-empty and square")
    n = len(matrix)
    return [matrix[0][i] for i in range(n)] + [
        matrix[row][n - 1 - row] for row in range(1, n - 1)
    ] + [matrix[n - 1][i] for i in range(n - 1, -1, -1)]

if __name__ == "__main__":
    print(z_form([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
