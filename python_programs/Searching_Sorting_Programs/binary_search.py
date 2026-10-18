def binary_search(values, target):
    low, high = 0, len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(values, target, low=0, high=None):
    if high is None:
        high = len(values) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if values[mid] == target:
        return mid
    if values[mid] < target:
        return binary_search_recursive(values, target, mid + 1, high)
    return binary_search_recursive(values, target, low, mid - 1)

if __name__ == "__main__":
    data = [1, 3, 5, 7, 9]
    print(binary_search(data, 7), binary_search_recursive(data, 3))
