from src.linked_list.without_tail.linked_list import LinkedList


def remove_duplicates(linked_list: LinkedList) -> LinkedList:
    """
    Remove duplicates from an unsorted linked list.
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

    return linked_list
