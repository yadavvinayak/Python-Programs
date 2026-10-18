def k_smallest_largest(values, k):
    if not 0 <= k <= len(values):
        raise ValueError("k must be between 0 and tuple length")
    ordered = sorted(values)
    return tuple(ordered[:k]), tuple(ordered[-k:] if k else [])

if __name__ == "__main__":
    print(k_smallest_largest((8, 1, 6, 3, 9), 2))
