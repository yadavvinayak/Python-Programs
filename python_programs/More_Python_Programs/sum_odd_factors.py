def sum_odd_factors(n):
    if n <= 0:
        raise ValueError("n must be positive")
    total = 0
    for factor in range(1, int(n ** 0.5) + 1):
        if n % factor == 0:
            other = n // factor
            if factor % 2:
                total += factor
            if other != factor and other % 2:
                total += other
    return total

if __name__ == "__main__":
    print(sum_odd_factors(int(input("n: "))))
