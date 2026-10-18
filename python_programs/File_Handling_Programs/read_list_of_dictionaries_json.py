import json
from pathlib import Path

def read_records(filename):
    data = json.loads(Path(filename).read_text(encoding="utf-8"))
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("file must contain a JSON list of objects")
    return data

if __name__ == "__main__":
    print(read_records(input("JSON file path: ")))
