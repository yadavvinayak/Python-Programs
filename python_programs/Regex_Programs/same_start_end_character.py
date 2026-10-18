def same_start_end(text):
    return bool(text) and text[0] == text[-1]

if __name__ == "__main__":
    print(same_start_end(input("Text: ")))
