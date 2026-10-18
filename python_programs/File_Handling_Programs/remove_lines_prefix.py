from pathlib import Path

def remove_prefix_lines(source, destination, prefix):
    lines = Path(source).read_text(encoding="utf-8").splitlines(keepends=True)
    Path(destination).write_text("".join(line for line in lines if not line.startswith(prefix)), encoding="utf-8")

if __name__ == "__main__":
    remove_prefix_lines(input("Source: "), input("Destination: "), input("Prefix: "))
