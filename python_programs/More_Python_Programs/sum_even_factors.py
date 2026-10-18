def sum_even_factors(n):
    if n <= 0:
        raise ValueError("n must be positive")
    return sum(factor for factor in range(2, n + 1, 2) if n % factor == 0)

if __name__ == "__main__":
    print(sum_even_factors(int(input("n: "))))
