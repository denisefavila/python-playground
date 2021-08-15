from src.linked_list.without_tail.linked_list import LinkedList


def reverse(linked_list: LinkedList) -> LinkedList:
    """
    Reverse the linked list.
    """
    current_node = linked_list.head
    previous_node = None

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node

        previous_node = current_node
        current_node = next_node

    linked_list.head = previous_node
    return linked_list
