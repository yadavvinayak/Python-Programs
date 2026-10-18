from pathlib import Path

def words_of_length(filename, length):
    return [word for word in Path(filename).read_text(encoding="utf-8").split() if len(word) == length]

if __name__ == "__main__":
    print(words_of_length(input("File path: "), int(input("Word length: "))))
