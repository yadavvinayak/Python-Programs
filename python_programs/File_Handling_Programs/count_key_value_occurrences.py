from pathlib import Path

def count_occurrences(filename, phrase):
    return Path(filename).read_text(encoding="utf-8").count(phrase)

if __name__ == "__main__":
    print(count_occurrences(input("File path: "), input("Text to count: ")))
