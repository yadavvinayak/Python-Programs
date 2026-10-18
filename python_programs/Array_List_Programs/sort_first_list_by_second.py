def sort_by_order(values, order):
    rank = {value: index for index, value in enumerate(order)}
    return sorted(values, key=lambda value: rank.get(value, len(rank)))

if __name__ == "__main__":
    print(sort_by_order(["a", "c", "b", "d"], ["b", "a", "c"]))
