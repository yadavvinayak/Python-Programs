def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return 0 if a == 0 or b == 0 else abs(a * b) // gcd(a, b)

if __name__ == "__main__":
    a, b = int(input("a: ")), int(input("b: "))
    print("GCD:", gcd(a, b), "LCM:", lcm(a, b))
