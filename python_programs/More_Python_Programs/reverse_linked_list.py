class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def reverse(head):
    previous, current = None, head
    while current:
        following = current.next
        current.next = previous
        previous, current = current, following
    return previous

def to_list(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values

if __name__ == "__main__":
    head = Node(1, Node(2, Node(3)))
    print(to_list(reverse(head)))
