def bitonic_sort(values):
    # Simple recursive bitonic sort; input length must be a power of two.
    result = list(values)
    n = len(result)
    if n == 0 or n & (n - 1):
        raise ValueError("length must be a power of two")
    def compare_and_swap(i, j, ascending):
        if (result[i] > result[j]) == ascending:
            result[i], result[j] = result[j], result[i]
    def merge(low, count, ascending):
        if count > 1:
            half = count // 2
            for i in range(low, low + half):
                compare_and_swap(i, i + half, ascending)
            merge(low, half, ascending)
            merge(low + half, half, ascending)
    def sort(low, count, ascending):
        if count > 1:
            half = count // 2
            sort(low, half, True)
            sort(low + half, half, False)
            merge(low, count, ascending)
    sort(0, n, True)
    return result

if __name__ == "__main__":
    print(bitonic_sort([3, 7, 4, 8, 6, 2, 1, 5]))
