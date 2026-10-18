def quicksort(values):
    result = list(values)
    stack = [(0, len(result) - 1)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        pivot = result[high]
        boundary = low
        for index in range(low, high):
            if result[index] <= pivot:
                result[boundary], result[index] = result[index], result[boundary]
                boundary += 1
        result[boundary], result[high] = result[high], result[boundary]
        stack.extend([(low, boundary - 1), (boundary + 1, high)])
    return result

if __name__ == "__main__":
    print(quicksort([5, 2, 8, 1, 4]))
