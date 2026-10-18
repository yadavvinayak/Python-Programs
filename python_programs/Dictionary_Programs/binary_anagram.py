def binary_anagram(a, b):
    return sorted(bin(a)[2:]) == sorted(bin(b)[2:])

if __name__ == "__main__":
    print(binary_anagram(12, 18))
