def radix_sort(values):
    if not values:
        return []
    if min(values) < 0:
        raise ValueError("radix_sort example supports non-negative integers")
    result = list(values)
    exp = 1
    while max(result) // exp > 0:
        output = [0] * len(result)
        counts = [0] * 10
        for value in result:
            counts[(value // exp) % 10] += 1
        for i in range(1, 10):
            counts[i] += counts[i - 1]
        for value in reversed(result):
            digit = (value // exp) % 10
            counts[digit] -= 1
            output[counts[digit]] = value
        result = output
        exp *= 10
    return result

if __name__ == "__main__":
    print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
