def has_consecutive_zeroes(number, base=2):
    if number < 0 or base < 2:
        raise ValueError("number must be non-negative and base >= 2")
    digits = []
    while number:
        digits.append(str(number % base))
        number //= base
    representation = "".join(reversed(digits)) or "0"
    return "00" in representation

if __name__ == "__main__":
    print(has_consecutive_zeroes(int(input("Number: ")), int(input("Base: "))))
