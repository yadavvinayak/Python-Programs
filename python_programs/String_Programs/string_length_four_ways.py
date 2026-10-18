def lengths(text):
    return {
        "len": len(text),
        "iteration": sum(1 for _ in text),
        "enumeration": sum(1 for _index, _char in enumerate(text)),
        "count_nonempty_slice": len(text[:])
    }

if __name__ == "__main__":
    print(lengths("Python"))
