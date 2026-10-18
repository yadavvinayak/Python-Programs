def make_keyed_records(keys, rows):
    return {key: dict(zip(keys, row)) for key, row in enumerate(rows)}

if __name__ == "__main__":
    print(make_keyed_records(["name", "age"], [["Ada", 36], ["Grace", 85]]))
