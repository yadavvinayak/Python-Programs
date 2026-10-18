from datetime import datetime

if __name__ == "__main__":
    value = datetime.strptime(input("Date (YYYY-MM-DD HH:MM:SS): "), "%Y-%m-%d %H:%M:%S")
    print(value.timestamp())
