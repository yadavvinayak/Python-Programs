def pigeonhole_sort(values):
    if not values:
        return []
    low, high = min(values), max(values)
    holes = [0] * (high - low + 1)
    for value in values:
        holes[value - low] += 1
    return [value + low for offset, count in enumerate(holes) for value in [offset] * count]

if __name__ == "__main__":
    print(pigeonhole_sort([8, 3, 2, 7, 4, 6, 8]))
