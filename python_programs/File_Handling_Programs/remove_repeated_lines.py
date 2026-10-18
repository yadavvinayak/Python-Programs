from pathlib import Path

def unique_lines(source, destination):
    seen, output = set(), []
    for line in Path(source).read_text(encoding="utf-8").splitlines(keepends=True):
        if line not in seen:
            seen.add(line)
            output.append(line)
    Path(destination).write_text("".join(output), encoding="utf-8")

if __name__ == "__main__":
    unique_lines(input("Source: "), input("Destination: "))
