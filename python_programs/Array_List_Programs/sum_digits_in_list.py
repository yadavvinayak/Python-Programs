def digit_sum(number):
    return sum(int(char) for char in str(abs(number)) if char.isdigit())

if __name__ == "__main__":
    print([digit_sum(number) for number in [12, 305, -48]])
