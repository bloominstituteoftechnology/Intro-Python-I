"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node

https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    if not head.next:
        return 0
    current_node = head
    visited = set()
    while current_node not in visited:
        visited.add(current_node)
        if not current_node.next:
            return 0
        current_node = current_node.next
    return 1


node1 = Node(1, None)

node4 = Node(4, None)
node2 = Node(2, None)
node3 = Node(3,  node2)
node4.next = node2
node2.next = node3

print(has_cycle(node1))
print(has_cycle(node4))
