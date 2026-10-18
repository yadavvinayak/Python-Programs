from pathlib import Path

def matching_lines(filename, word):
    return [(number, line.rstrip()) for number, line in enumerate(
        Path(filename).read_text(encoding="utf-8").splitlines(), start=1) if word in line]

if __name__ == "__main__":
    print(matching_lines(input("File path: "), input("Word: ")))
