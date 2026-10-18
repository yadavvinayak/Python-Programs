from operator import itemgetter

if __name__ == "__main__":
    records = [{"name": "A", "score": 8}, {"name": "B", "score": 5}]
    print(sorted(records, key=itemgetter("score")))
