def rotate_left_in_place(values, steps):
    if not values:
        return values
    steps %= len(values)
    values[:steps] = reversed(values[:steps])
    values[steps:] = reversed(values[steps:])
    values.reverse()
    return values

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(rotate_left_in_place(data, 2))
