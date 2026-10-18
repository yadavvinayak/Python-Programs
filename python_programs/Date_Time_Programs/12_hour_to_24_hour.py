from datetime import datetime

def to_24_hour(time_text):
    return datetime.strptime(time_text, "%I:%M:%S %p").strftime("%H:%M:%S")

if __name__ == "__main__":
    print(to_24_hour(input("Time (e.g. 07:30:00 PM): ")))
