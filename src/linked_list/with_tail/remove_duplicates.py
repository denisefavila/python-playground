from src.linked_list.with_tail.linked_list import LinkedListWithTail


def remove_duplicates(linked_list: LinkedListWithTail) -> LinkedListWithTail:
    """
    Remove duplicates from an unsorted linked list with tail implementation.
    Reference: Cracking the Code Interview
    """
    visited = set()

    current_node = linked_list.head
    previous_node = None

    while current_node:
        if current_node.item in visited:
            previous_node.next = current_node.next

        else:
            visited.add(current_node.item)
            previous_node = current_node

        current_node = current_node.next
    linked_list.tail = previous_node
    return linked_list
