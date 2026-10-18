def chunks(values, size):
    if size <= 0:
        raise ValueError("size must be positive")
    return [values[i:i + size] for i in range(0, len(values), size)]

if __name__ == "__main__":
    print(chunks([1, 2, 3, 4, 5, 6, 7], 3))
