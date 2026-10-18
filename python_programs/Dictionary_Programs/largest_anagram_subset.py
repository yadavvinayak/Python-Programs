from collections import Counter

def largest_anagram_subset_size(words):
    signatures = Counter("".join(sorted(word.casefold())) for word in words)
    return max(signatures.values(), default=0)

if __name__ == "__main__":
    print(largest_anagram_subset_size(["cat", "act", "dog", "tac"]))
