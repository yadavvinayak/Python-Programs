from pathlib import Path

def copy_odd_lines(source, destination):
    lines = Path(source).read_text(encoding="utf-8").splitlines(keepends=True)
    Path(destination).write_text("".join(lines[::2]), encoding="utf-8")

if __name__ == "__main__":
    copy_odd_lines(input("Source: "), input("Destination: "))
