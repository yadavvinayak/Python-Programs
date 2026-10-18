def matching_characters(first, second):
    return set(first) & set(second)

if __name__ == "__main__":
    print(matching_characters("hello", "world"))
