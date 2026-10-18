def extended_gcd(a, b):
    if b == 0:
        return abs(a), 1 if a >= 0 else -1, 0
    gcd_value, x1, y1 = extended_gcd(b, a % b)
    return gcd_value, y1, x1 - (a // b) * y1

if __name__ == "__main__":
    a, b = int(input("a: ")), int(input("b: "))
    print("gcd, x, y:", extended_gcd(a, b))
