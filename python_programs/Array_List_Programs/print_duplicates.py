from collections import Counter

def duplicates(values):
    return [value for value, count in Counter(values).items() if count > 1]

if __name__ == "__main__":
    print(duplicates([1, 2, 2, 3, 1, 4]))
