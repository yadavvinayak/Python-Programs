def difference(number):
    odd = even = 0
    for char in str(abs(number)):
        digit = int(char)
        if digit % 2:
            odd += digit
        else:
            even += digit
    return odd - even

if __name__ == "__main__":
    print(difference(int(input("Integer: "))))
