def cycle_sort(values):
    result = list(values)
    writes = 0
    for cycle_start in range(len(result) - 1):
        item = result[cycle_start]
        position = cycle_start
        for i in range(cycle_start + 1, len(result)):
            if result[i] < item:
                position += 1
        if position == cycle_start:
            continue
        while item == result[position]:
            position += 1
        result[position], item = item, result[position]
        writes += 1
        while position != cycle_start:
            position = cycle_start
            for i in range(cycle_start + 1, len(result)):
                if result[i] < item:
                    position += 1
            while item == result[position]:
                position += 1
            result[position], item = item, result[position]
            writes += 1
    return result

if __name__ == "__main__":
    print(cycle_sort([1, 8, 3, 9, 10, 10, 2, 4]))
