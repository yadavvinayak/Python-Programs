from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))

def primes_between_squares(n):
    if n < 1:
        raise ValueError("n must be positive")
    return [value for value in range(n * n + 1, (n + 1) ** 2) if is_prime(value)]

if __name__ == "__main__":
    n = int(input("Positive integer n: "))
    print(primes_between_squares(n))
