import heapq

def heap_sort(values):
    heap = list(values)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]

if __name__ == "__main__":
    print(heap_sort([4, 10, 3, 5, 1]))
