def cube_sum(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    return (n * (n + 1) // 2) ** 2

if __name__ == "__main__":
    print(cube_sum(int(input("n: "))))
