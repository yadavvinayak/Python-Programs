def all_digits_divide(number):
    if number == 0:
        return False
    digits = [int(char) for char in str(abs(number))]
    return all(digit != 0 and number % digit == 0 for digit in digits)

if __name__ == "__main__":
    print(all_digits_divide(int(input("Integer: "))))
