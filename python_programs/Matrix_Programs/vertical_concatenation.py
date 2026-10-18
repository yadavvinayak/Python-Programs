def vertical_concatenate(*matrices):
    if not matrices:
        return []
    width = len(matrices[0][0]) if matrices[0] else 0
    if any(any(len(row) != width for row in matrix) for matrix in matrices):
        raise ValueError("all rows must have equal width")
    return [row[:] for matrix in matrices for row in matrix]

if __name__ == "__main__":
    print(vertical_concatenate([[1, 2]], [[3, 4], [5, 6]]))
