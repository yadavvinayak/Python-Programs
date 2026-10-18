def swap(values, first, second):
    result = list(values)
    result[first], result[second] = result[second], result[first]
    return result

if __name__ == "__main__":
    print(swap([1, 2, 3, 4], 0, 2))
