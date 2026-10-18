from math import isqrt

def primes_in_interval(start, end):
    result = []
    for number in range(max(2, start), end + 1):
        if all(number % divisor for divisor in range(2, isqrt(number) + 1)):
            result.append(number)
    return result

if __name__ == "__main__":
    print(primes_in_interval(int(input("Start: ")), int(input("End: "))))
