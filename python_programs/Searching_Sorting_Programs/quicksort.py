def quicksort(values):
    if len(values) < 2:
        return list(values)
    pivot = values[len(values) // 2]
    less = [value for value in values if value < pivot]
    equal = [value for value in values if value == pivot]
    greater = [value for value in values if value > pivot]
    return quicksort(less) + equal + quicksort(greater)

if __name__ == "__main__":
    print(quicksort([3, 6, 1, 8, 2, 3]))
