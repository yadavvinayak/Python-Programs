from functools import reduce
from operator import mul

def product_remainder(values, modulus):
    if modulus == 0:
        raise ValueError("modulus cannot be zero")
    product = reduce(mul, values, 1)
    return product % modulus

if __name__ == "__main__":
    print(product_remainder([2, 3, 4], 5))
