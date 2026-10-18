def gnome_sort(values):
    result = list(values)
    index = 0
    while index < len(result):
        if index == 0 or result[index] >= result[index - 1]:
            index += 1
        else:
            result[index], result[index - 1] = result[index - 1], result[index]
            index -= 1
    return result

if __name__ == "__main__":
    print(gnome_sort([34, 2, 10, -9]))
