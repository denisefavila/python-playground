from typing import Optional

from src.linked_list.node import Node


def swap_pairs(head: Optional[Node]) -> Optional[Node]:

    """
    Given a linked list, swap every two adjacent nodes and return its head.
    You must solve the problem without modifying the values in the list's nodes
    (i.e., only nodes themselves may be changed.)
    """

    dummy = previous_node = Node(0, head)

    while previous_node.next and previous_node.next.next:
        current_node = previous_node.next
        next_node = current_node.next

        previous_node.next = current_node.next
        current_node.next = next_node.next
        next_node.next = current_node

        previous_node = current_node

    return dummy.next
