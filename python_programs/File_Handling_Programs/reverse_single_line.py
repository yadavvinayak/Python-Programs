from pathlib import Path

def reverse_line(source, destination):
    lines = Path(source).read_text(encoding="utf-8").splitlines()
    Path(destination).write_text((lines[0][::-1] if lines else "") + "\n", encoding="utf-8")

if __name__ == "__main__":
    reverse_line(input("Source: "), input("Destination: "))
