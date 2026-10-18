def order_by_external(items, order):
    rank = {value: index for index, value in enumerate(order)}
    return sorted(items, key=lambda item: rank.get(item[0], len(rank)))

if __name__ == "__main__":
    print(order_by_external([("b", 2), ("a", 1), ("c", 3)], ["a", "b", "c"]))
