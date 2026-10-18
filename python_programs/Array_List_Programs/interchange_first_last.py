def interchange_first_last(values):
    result = list(values)
    if len(result) > 1:
        result[0], result[-1] = result[-1], result[0]
    return result

if __name__ == "__main__":
    print(interchange_first_last([10, 20, 30, 40]))
