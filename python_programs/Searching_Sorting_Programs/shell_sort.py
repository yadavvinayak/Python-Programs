def shell_sort(values):
    result = list(values)
    gap = len(result) // 2
    while gap:
        for i in range(gap, len(result)):
            current = result[i]
            j = i
            while j >= gap and result[j - gap] > current:
                result[j] = result[j - gap]
                j -= gap
            result[j] = current
        gap //= 2
    return result

if __name__ == "__main__":
    print(shell_sort([12, 34, 54, 2, 3]))
