def split_and_rotate(values, split_at):
    if not values:
        return []
    split_at %= len(values)
    return values[split_at:] + values[:split_at]

if __name__ == "__main__":
    print(split_and_rotate([1, 2, 3, 4, 5], 2))
