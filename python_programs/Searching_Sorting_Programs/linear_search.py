def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

if __name__ == "__main__":
    print(linear_search([4, 8, 2, 9], 2))
