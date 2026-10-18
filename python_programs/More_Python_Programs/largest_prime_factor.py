def largest_prime_factor(n):
    if n < 2:
        raise ValueError("n must be at least 2")
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor += 1 if factor == 2 else 2
    return n

if __name__ == "__main__":
    print(largest_prime_factor(int(input("n: "))))
