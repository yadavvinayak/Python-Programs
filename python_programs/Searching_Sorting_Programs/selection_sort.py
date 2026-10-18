def selection_sort(values):
    result = list(values)
    for i in range(len(result)):
        smallest = min(range(i, len(result)), key=result.__getitem__, default=i)
        result[i], result[smallest] = result[smallest], result[i]
    return result

if __name__ == "__main__":
    print(selection_sort([64, 25, 12, 22, 11]))
