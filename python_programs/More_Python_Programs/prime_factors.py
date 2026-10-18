def prime_factors(n):
    if n < 2:
        return []
    factors, divisor = [], 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1 if divisor == 2 else 2
    if n > 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    print(prime_factors(int(input("n: "))))
