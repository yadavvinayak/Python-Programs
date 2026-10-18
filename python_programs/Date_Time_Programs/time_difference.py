from datetime import datetime

def difference_from_now(time_text, fmt="%Y-%m-%d %H:%M:%S"):
    target = datetime.strptime(time_text, fmt)
    now = datetime.now()
    return target - now

if __name__ == "__main__":
    print(difference_from_now(input("Target time (YYYY-MM-DD HH:MM:SS): ")))
