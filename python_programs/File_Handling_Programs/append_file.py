from pathlib import Path

def append_file(source, destination):
    with Path(destination).open("a", encoding="utf-8") as target:
        target.write(Path(source).read_text(encoding="utf-8"))

if __name__ == "__main__":
    append_file(input("Source: "), input("Destination: "))
