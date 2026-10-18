import random

def bogo_sort(values, max_shuffles=100_000):
                                                                         
    result = list(values)
    for _ in range(max_shuffles):
        if result == sorted(result):
            return result
        random.shuffle(result)
    raise RuntimeError("max_shuffles reached; input not sorted")

if __name__ == "__main__":
    print(bogo_sort([2, 1, 3]))
