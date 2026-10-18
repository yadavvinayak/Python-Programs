from collections import OrderedDict

def insert_at_beginning(mapping, key, value):
    result = OrderedDict([(key, value)])
    result.update((k, v) for k, v in mapping.items() if k != key)
    return result

if __name__ == "__main__":
    print(insert_at_beginning(OrderedDict([("b", 2), ("c", 3)]), "a", 1))
