from collections import defaultdict

def join_by_first(items):
    groups = defaultdict(list)
    for item in items:
        groups[item[0]].append(item)
    return [tuple(value for item in group for value in item[1:]) for group in groups.values()]

if __name__ == "__main__":
    print(join_by_first([(1, "a"), (1, "b"), (2, "c")]))
