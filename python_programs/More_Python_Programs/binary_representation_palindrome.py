def is_binary_palindrome(number):
    if number < 0:
        return False
    binary = bin(number)[2:]
    return binary == binary[::-1]

if __name__ == "__main__":
    print(is_binary_palindrome(int(input("Integer: "))))
