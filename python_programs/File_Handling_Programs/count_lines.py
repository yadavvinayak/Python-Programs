from pathlib import Path

if __name__ == "__main__":
    path = Path(input("File path: "))
    print("Lines:", len(path.read_text(encoding="utf-8").splitlines()))
