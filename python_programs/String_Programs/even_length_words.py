def even_length_words(text):
    return [word for word in text.split() if len(word) % 2 == 0]

if __name__ == "__main__":
    print(even_length_words("Python is a great language"))
