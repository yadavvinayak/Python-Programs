def sort_dictionary(mapping, by="key"):
    if by == "key":
        return dict(sorted(mapping.items()))
    if by == "value":
        return dict(sorted(mapping.items(), key=lambda item: item[1]))
    raise ValueError("by must be 'key' or 'value'")

if __name__ == "__main__":
    print(sort_dictionary({"b": 2, "a": 3, "c": 1}, "value"))
