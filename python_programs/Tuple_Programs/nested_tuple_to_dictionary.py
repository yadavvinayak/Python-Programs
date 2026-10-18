def nested_to_dict(items):
    return {key: value for key, value in items}

if __name__ == "__main__":
    print(nested_to_dict((("name", "Ada"), ("age", 36))))
