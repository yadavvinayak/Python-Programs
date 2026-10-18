from collections import Counter

def kth_non_repeating(text, k):
    if k < 1:
        raise ValueError("k is 1-based")
    counts = Counter(text)
    unique = [char for char in text if counts[char] == 1]
    return unique[k - 1] if len(unique) >= k else None

if __name__ == "__main__":
    print(kth_non_repeating("geeksforgeeks", 3))
