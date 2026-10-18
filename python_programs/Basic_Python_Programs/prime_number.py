def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True

if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    print("Prime" if is_prime(n) else "Not prime")
