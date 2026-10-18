from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        groups["".join(sorted(word.casefold()))].append(word)
    return list(groups.values())

if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
