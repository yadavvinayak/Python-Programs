from pathlib import Path

def count_file(filename):
    text = Path(filename).read_text(encoding="utf-8")
    return {"characters": len(text), "words": len(text.split()),
            "spaces": text.count(" "), "lines": len(text.splitlines())}

if __name__ == "__main__":
    print(count_file(input("File path: ")))
