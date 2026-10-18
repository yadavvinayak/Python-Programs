def triangle_possible(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b + c == 180

if __name__ == "__main__":
    print(triangle_possible(int(input("Angle 1: ")), int(input("Angle 2: ")), int(input("Angle 3: "))))
