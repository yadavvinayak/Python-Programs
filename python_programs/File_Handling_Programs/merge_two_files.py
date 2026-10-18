from pathlib import Path

def merge_files(first, second, destination):
    content = Path(first).read_text(encoding="utf-8") + Path(second).read_text(encoding="utf-8")
    Path(destination).write_text(content, encoding="utf-8")

if __name__ == "__main__":
    merge_files(input("First file: "), input("Second file: "), input("Destination: "))
