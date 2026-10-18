def combine(a, b, operation="add"):
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise ValueError("matrices must have equal dimensions")
    if operation not in {"add", "subtract"}:
        raise ValueError("operation must be add or subtract")
    sign = 1 if operation == "add" else -1
    return [[x + sign * y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]

if __name__ == "__main__":
    a, b = [[1, 2], [3, 4]], [[5, 6], [7, 8]]
    print("Sum:", combine(a, b))
    print("Difference:", combine(a, b, "subtract"))
