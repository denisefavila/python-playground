from dataclasses import dataclass
from typing import Any, Hashable


@dataclass
class Node:
    key: Hashable
    value: Any
    next: Any = None


class Hashtable:
    """
    Implements a simple hashtable using a linked list and a hash code
    function.
    """
    def __init__(self, size: int):
        self.size = size
        self.buckets = [None]*self.size

    def __setitem__(self, key: Hashable, value: Any) -> None:
        idx = hash(key) % self.size

        node = self.buckets[idx]
        if not node:
            # The linked list is empty, insert at the first position.
            self.buckets[idx] = Node(key=key, value=value)
            return

        # Collision! We go until the end and add the node.
        aux = node
        while node and node.key != key:
            aux = node
            node = node.next

        if not node:
            # Got to the end, add new node.
            aux.next = Node(key=key, value=value)
        else:
            # Found node we same key.
            node.value = value

    def __getitem__(self, key: Hashable) -> Any:
        idx = hash(key) % self.size
        node = self.buckets[idx]

        while node and node.key != key:
            node = node.next

        if not node:
            raise KeyError
        else:
            return node.value


