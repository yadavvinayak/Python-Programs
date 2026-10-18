def ordered_items(mapping):
    return [(key, mapping[key]) for key in mapping]

if __name__ == "__main__":
    print(ordered_items({"name": "Ada", "age": 36}))
