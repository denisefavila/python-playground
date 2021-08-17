from typing import Union, Any

from src.linked_list.node import Node


def remove_kth_to_last(head: Node, k: int) -> Union[Any, None]:
    """
    Find the kth to last element of a singly linked list.
    Reference: Cracking the Code Interview
    O(n)
    """

    dummy = Node(0, head)
    slow = fast = dummy

    if not head:
        return

    for _ in range(k):
        try:
            fast = fast.next
        except AttributeError:
            return head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next
