from pathlib import Path

def read_characters(filename):
    with Path(filename).open(encoding="utf-8") as file:
        while char := file.read(1):
            print(repr(char))

if __name__ == "__main__":
    read_characters(input("File path: "))
