def maximum(a, b):
    return a if a >= b else b

if __name__ == "__main__":
    print("Maximum:", maximum(float(input("First number: ")), float(input("Second number: "))))
