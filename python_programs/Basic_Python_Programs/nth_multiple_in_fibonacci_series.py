def first_fibonacci_multiple_of(k, limit=1_000_000):
    if k == 0:
        raise ValueError("k must be non-zero")
    a, b = 0, 1
    for index in range(limit + 1):
        if a != 0 and a % k == 0:
            return index, a
        a, b = b, a + b
    return None

if __name__ == "__main__":
    k = int(input("Find a non-zero Fibonacci number divisible by: "))
    print(first_fibonacci_multiple_of(k) or "No result within search limit")
