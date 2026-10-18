def remove_empty_tuples(values):
    return [value for value in values if value != ()]

if __name__ == "__main__":
    print(remove_empty_tuples([(), (1, 2), (), (3,)]))
