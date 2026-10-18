from pathlib import Path

def reverse_lines(source, destination):
    stack = Path(source).read_text(encoding="utf-8").splitlines()
    Path(destination).write_text("\n".join(reversed(stack)) + ("\n" if stack else ""), encoding="utf-8")

if __name__ == "__main__":
    reverse_lines(input("Source: "), input("Destination: "))
