def cocktail_sort(values):
    result = list(values)
    start, end = 0, len(result) - 1
    while start < end:
        swapped = False
        for i in range(start, end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]; swapped = True
        end -= 1
        for i in range(end, start, -1):
            if result[i] < result[i - 1]:
                result[i], result[i - 1] = result[i - 1], result[i]; swapped = True
        start += 1
        if not swapped:
            break
    return result

if __name__ == "__main__":
    print(cocktail_sort([5, 1, 4, 2, 8, 0, 2]))
