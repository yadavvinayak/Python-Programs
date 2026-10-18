import math

def area(radius):
    if radius < 0:
        raise ValueError("radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == "__main__":
    print("Area:", area(float(input("Radius: "))))
