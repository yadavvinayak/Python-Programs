def remove_values(values, unwanted):
    unwanted = set(unwanted)
    return [value for value in values if value not in unwanted]

if __name__ == "__main__":
    print(remove_values([1, 2, 3, 2, 4], [2, 4]))
