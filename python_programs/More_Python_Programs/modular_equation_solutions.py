def count_solutions(a, b, modulus):
    # Counts x in [0, modulus-1] satisfying a*x == b (mod modulus).
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    return sum((a * x - b) % modulus == 0 for x in range(modulus))

if __name__ == "__main__":
    print(count_solutions(3, 6, 9))
