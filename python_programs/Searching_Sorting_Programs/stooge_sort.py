def stooge_sort(values):
    result = list(values)
    def sort(low, high):
        if result[low] > result[high]:
            result[low], result[high] = result[high], result[low]
        if high - low + 1 > 2:
            third = (high - low + 1) // 3
            sort(low, high - third)
            sort(low + third, high)
            sort(low, high - third)
    if result:
        sort(0, len(result) - 1)
    return result

if __name__ == "__main__":
    print(stooge_sort([2, 4, 5, 3, 1]))
