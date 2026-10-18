def merge_sort(values):
    if len(values) <= 1:
        return list(values)
    mid = len(values) // 2
    left, right = merge_sort(values[:mid]), merge_sort(values[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    return merged + left[i:] + right[j:]

if __name__ == "__main__":
    print(merge_sort([9, 3, 7, 1, 5]))
