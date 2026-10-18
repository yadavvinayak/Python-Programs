def is_armstrong(n):
    digits = str(abs(n))
    power = len(digits)
    return n >= 0 and sum(int(digit) ** power for digit in digits) == n

if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    print("Armstrong number" if is_armstrong(number) else "Not an Armstrong number")
