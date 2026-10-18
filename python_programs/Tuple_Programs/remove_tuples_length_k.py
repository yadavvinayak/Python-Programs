def remove_length_k(items, k):
    return [item for item in items if len(item) != k]

if __name__ == "__main__":
    print(remove_length_k([(1,), (1, 2), (3, 4, 5)], 2))
