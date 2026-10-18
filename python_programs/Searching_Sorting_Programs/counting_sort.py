def counting_sort(values):
    if not values:
        return []
    low, high = min(values), max(values)
    counts = [0] * (high - low + 1)
    for value in values:
        counts[value - low] += 1
    return [value + low for offset, count in enumerate(counts) for value in [offset] * count]

if __name__ == "__main__":
    print(counting_sort([4, -1, 2, 4, 0, -1]))
