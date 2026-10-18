from bisect import bisect_right

def binary_insertion_sort(values):
    result = []
    for value in values:
        result.insert(bisect_right(result, value), value)
    return result

if __name__ == "__main__":
    print(binary_insertion_sort([5, 2, 4, 1, 3]))
