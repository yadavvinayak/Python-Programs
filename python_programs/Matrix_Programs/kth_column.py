def kth_column(matrix, k):
    if not matrix or k < 0 or any(k >= len(row) for row in matrix):
        raise IndexError("column index out of range")
    return [row[k] for row in matrix]

if __name__ == "__main__":
    print(kth_column([[1, 2], [3, 4], [5, 6]], 1))
