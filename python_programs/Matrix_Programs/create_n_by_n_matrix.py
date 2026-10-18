def create_matrix(n, fill=0):
    if n < 0:
        raise ValueError("n must be non-negative")
    return [[fill for _ in range(n)] for _ in range(n)]

if __name__ == "__main__":
    print(create_matrix(3))
