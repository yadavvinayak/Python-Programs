def largest(values):
    if not values:
        raise ValueError("list cannot be empty")
    return max(values)

if __name__ == "__main__":
    print(largest([int(x) for x in input("Integers separated by spaces: ").split()]))
