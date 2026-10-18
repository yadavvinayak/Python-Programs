def smallest(values):
    if not values:
        raise ValueError("list cannot be empty")
    return min(values)

if __name__ == "__main__":
    print(smallest([8, 2, 5, -1]))
