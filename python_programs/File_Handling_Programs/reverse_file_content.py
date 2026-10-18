from pathlib import Path

def reverse_content(source, destination):
    text = Path(source).read_text(encoding="utf-8")
    Path(destination).write_text(text[::-1], encoding="utf-8")

if __name__ == "__main__":
    reverse_content(input("Source: "), input("Destination: "))
