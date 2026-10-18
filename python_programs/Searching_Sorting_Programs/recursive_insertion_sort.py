def recursive_insertion_sort(values, n=None):
    result = list(values)
    if n is None:
        n = len(result)
    if n <= 1:
        return result
    result = recursive_insertion_sort(result, n - 1)
    last = result[n - 1]
    j = n - 2
    while j >= 0 and result[j] > last:
        result[j + 1] = result[j]
        j -= 1
    result[j + 1] = last
    return result

if __name__ == "__main__":
    print(recursive_insertion_sort([4, 2, 5, 1, 3]))
