def print_double_staircase(rows):
    for row in range(1, rows + 1):
        print(" " * (rows - row) + "*" * row + "  " + "*" * row)

if __name__ == "__main__":
    print_double_staircase(int(input("Rows: ")))
