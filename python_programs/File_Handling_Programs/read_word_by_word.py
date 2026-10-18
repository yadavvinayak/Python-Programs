from pathlib import Path

def read_words(filename):
    for word in Path(filename).read_text(encoding="utf-8").split():
        print(word)

if __name__ == "__main__":
    read_words(input("File path: "))
