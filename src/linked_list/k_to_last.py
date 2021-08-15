from typing import Union, Any

from src.linked_list.linked_list import LinkedList


def kth_to_last(linked_list: LinkedList, k: int) -> Union[Any, None]:
    """
    Find the kth to last element of a singly linked list.
    Reference: Cracking the Code Interview
    In fact, using my implementation for LinkedList (as I'm saving the linked list size)
    this is really trivial. But, I'm ignoring it and implementing this function
    considering that we don't have the size, just to practice.
    O(n^2)
    """

    if k > len(linked_list) - 1:
        return None

    current_node = aux = linked_list.head

    while current_node:

        for _ in range(k):
            aux = aux.next

        if not aux.next:
            return current_node.item

        current_node = current_node.next
        aux = current_node
