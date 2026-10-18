from prime_factors import prime_factors

def product_unique_factors(n):
    result = 1
    for factor in set(prime_factors(n)):
        result *= factor
    return result

if __name__ == "__main__":
    print(product_unique_factors(int(input("n: "))))
