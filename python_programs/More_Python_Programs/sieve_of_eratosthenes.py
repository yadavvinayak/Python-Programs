def primes_up_to(limit):
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if sieve[number]:
            sieve[number * number:limit + 1:number] = [False] * len(range(number * number, limit + 1, number))
    return [number for number, prime in enumerate(sieve) if prime]

if __name__ == "__main__":
    print(primes_up_to(int(input("Limit: "))))
