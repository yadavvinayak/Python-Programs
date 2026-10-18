from collections import deque

def topological_sort(graph):
    indegree = {node: 0 for node in graph}
    for neighbors in graph.values():
        for neighbor in neighbors:
            indegree[neighbor] = indegree.get(neighbor, 0) + 1
    queue = deque(node for node, degree in indegree.items() if degree == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) != len(indegree):
        raise ValueError("graph contains a cycle")
    return order

if __name__ == "__main__":
    print(topological_sort({"a": ["c"], "b": ["c"], "c": ["d"], "d": []}))
