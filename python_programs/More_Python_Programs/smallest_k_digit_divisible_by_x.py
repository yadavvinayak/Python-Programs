def smallest_k_digit_multiple(k, x):
    if k < 1 or x <= 0:
        raise ValueError("k must be positive and x must be positive")
    start = 10 ** (k - 1)
    return ((start + x - 1) // x) * x

if __name__ == "__main__":
    print(smallest_k_digit_multiple(int(input("Digits k: ")), int(input("Divisor x: "))))
