from typing import Optional

from src.linked_list.node import Node


def reverse(head: Optional[Node]) -> Optional[Node]:
    """
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    https://leetcode.com/problems/reverse-linked-list/
    """

    previous_node = None

    while head:
        next_node = head.next
        head.next = previous_node
        previous_node = head
        head = next_node

    return previous_node


