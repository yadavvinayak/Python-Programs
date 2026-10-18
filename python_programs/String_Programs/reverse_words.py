def reverse_words(text):
    return " ".join(text.split()[::-1])

if __name__ == "__main__":
    print(reverse_words("Python makes programming fun"))
