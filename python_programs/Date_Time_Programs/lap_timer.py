from time import perf_counter

if __name__ == "__main__":
    start = perf_counter()
    input("Press Enter to record a lap (Ctrl+C to stop)...")
    print("Lap:", round(perf_counter() - start, 3), "seconds")
