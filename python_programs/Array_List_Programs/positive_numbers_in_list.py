def positives(values):
    return [value for value in values if value > 0]

if __name__ == "__main__":
    print(positives([-2, 0, 3, 7, -1]))
