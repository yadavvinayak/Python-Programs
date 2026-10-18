from datetime import datetime

if __name__ == "__main__":
    timestamp = float(input("Unix timestamp: "))
    print(datetime.fromtimestamp(timestamp).astimezone().isoformat())
