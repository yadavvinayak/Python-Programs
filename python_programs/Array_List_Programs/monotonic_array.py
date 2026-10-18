def is_monotonic(values):
    return all(a <= b for a, b in zip(values, values[1:])) or all(
        a >= b for a, b in zip(values, values[1:])
    )

if __name__ == "__main__":
    print(is_monotonic([1, 2, 2, 4]))
