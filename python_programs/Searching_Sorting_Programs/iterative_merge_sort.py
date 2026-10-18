def merge_sort(values):
    result = list(values)
    width = 1
    while width < len(result):
        merged = []
        for start in range(0, len(result), 2 * width):
            left = result[start:start + width]
            right = result[start + width:start + 2 * width]
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i]); i += 1
                else:
                    merged.append(right[j]); j += 1
            merged.extend(left[i:]); merged.extend(right[j:])
        result = merged
        width *= 2
    return result

if __name__ == "__main__":
    print(merge_sort([9, 3, 7, 1, 5]))
