def odd_even_sort(values):
    result = list(values)
    sorted_flag = False
    while not sorted_flag:
        sorted_flag = True
        for start in (1, 0):
            for i in range(start, len(result) - 1, 2):
                if result[i] > result[i + 1]:
                    result[i], result[i + 1] = result[i + 1], result[i]
                    sorted_flag = False
    return result

if __name__ == "__main__":
    print(odd_even_sort([5, 1, 4, 2, 8, 0, 2]))
