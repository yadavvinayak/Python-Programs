def numbers_and_cubes(n):
    return tuple((value, value ** 3) for value in range(1, n + 1))

if __name__ == "__main__":
    print(numbers_and_cubes(5))
