def series(n):
    # Recursive example; output size is still O(n).
    if n <= 0:
        return []
    return series(n - 1) + [n]

if __name__ == "__main__":
    print(series(int(input("n: "))))
