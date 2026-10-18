def closest_value(values, target):
    if not values:
        raise ValueError("tuple cannot be empty")
    return min(values, key=lambda value: abs(value - target))

if __name__ == "__main__":
    print(closest_value((2, 8, 11, 15), 10))
