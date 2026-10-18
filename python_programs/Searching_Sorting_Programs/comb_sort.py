def comb_sort(values):
    result = list(values)
    gap, swapped = len(result), True
    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False
        for i in range(len(result) - gap):
            if result[i] > result[i + gap]:
                result[i], result[i + gap] = result[i + gap], result[i]
                swapped = True
    return result

if __name__ == "__main__":
    print(comb_sort([8, 4, 1, 56, 3, -44, 23]))
