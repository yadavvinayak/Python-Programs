def bubble_sort(values):
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        changed = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                changed = True
        if not changed:
            break
    return result

if __name__ == "__main__":
    print(bubble_sort([5, 1, 4, 2, 8]))
