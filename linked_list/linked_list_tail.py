
from typing import Any, Union

from node import Node


class LinkedList:

    """
    Implement a single linked list using head and tail info.
    """

    def __init__(self):
        self.size: int = 0
        self.head: Union[Node, None] = None
        self.tail: Union[Node, None] = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __repr__(self):
        values = [str(x) for x in self]
        return " -> ".join(values)

    def __len__(self):
        return self.size

    # Inserts an item at the beginning. O(1)
    def push_front(self, item: Any) -> None:
        if not self.head:
            self.head = self.tail = Node(item=item)
        else:
            self.head = Node(item=item, next=self.head)
        self.size += 1

    # Inserts an item at the end. O(1)
    def push_back(self, item: Any) -> None:
        new_node = Node(item=item)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.size += 1

    # Remove item at the beginning. O(1)
    def pop_front(self) -> None:
        aux = self.head
        if aux:
            self.head = aux.next
            if not aux.next:
                self.tail = None
            self.size -= 1

    # Remove item at the end. O(n)
    def pop_back(self) -> None:

        # Empty linked list
        if not self.head:
            return

        # Check if head need to be removed
        if not self.head.next:
            self.head = None
            self.tail = None
            return

        last_node = self.head
        # transverse the linked list
        while last_node:
            next_node = last_node.next
            if next_node == self.tail:
                break
            last_node = next_node

        last_node.next = None

        self.tail = last_node
        self.size -= 1
