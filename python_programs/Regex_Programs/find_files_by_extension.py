from pathlib import Path

def find_files(directory, extension):
    return sorted(path for path in Path(directory).rglob("*") if path.is_file() and path.suffix == extension)

if __name__ == "__main__":
    print(*find_files(".", ".py"), sep="\n")
