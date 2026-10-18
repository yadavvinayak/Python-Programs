def negative_range(start, end):
    return [n for n in range(start, end + 1) if n < 0]

if __name__ == "__main__":
    print(negative_range(-5, 5))
