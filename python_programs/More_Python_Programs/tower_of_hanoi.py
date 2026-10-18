def hanoi(n, source="A", auxiliary="B", target="C"):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n:
        yield from hanoi(n - 1, source, target, auxiliary)
        yield source, target
        yield from hanoi(n - 1, auxiliary, source, target)

if __name__ == "__main__":
    for move in hanoi(int(input("Number of disks: "))):
        print(f"{move[0]} -> {move[1]}")
