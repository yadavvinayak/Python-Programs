def print_inverted_triangle(rows):
    for width in range(rows, 0, -1):
        print("* " * width)

if __name__ == "__main__":
    print_inverted_triangle(int(input("Rows: ")))
