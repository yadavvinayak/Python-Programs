from itertools import product

if __name__ == "__main__":
    first, second = (1, 2), ("a", "b")
    print(list(product(first, second)))
