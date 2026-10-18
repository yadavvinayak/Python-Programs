from functools import reduce

def matrix_product(*matrices):
    if not matrices:
        raise ValueError("provide at least one matrix")
    result = matrices[0]
    for matrix in matrices[1:]:
        from multiply_matrices import multiply_matrices
        result = multiply_matrices(result, matrix)
    return result

if __name__ == "__main__":
    print(matrix_product([[1, 2]], [[3], [4]]))
