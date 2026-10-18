if __name__ == "__main__":
    values = (1, 2, 3)
    as_list = list(values) + [4]
    back_to_tuple = tuple(as_list)
    print(as_list, back_to_tuple)
