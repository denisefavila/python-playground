from src.linked_list.with_tail.linked_list import LinkedListWithTail


def remove_duplicates(linked_list: LinkedListWithTail) -> LinkedListWithTail:
    """
    Remove duplicates from an unsorted linked list with tail implementation.
    O(n)
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


def remove_duplicates_without_buffer(linked_list: LinkedListWithTail) -> LinkedListWithTail:
    """
    Remove duplicates from an unsorted linked list with tail implementation.
    Don't use an additional buffer;
    O(n^2)
    Reference: Cracking the Code Interview
    """

    current_node = aux = linked_list.head

    while current_node:
        aux = current_node
        while aux.next:
            if aux.next.item == current_node.item:
                current_node.next = aux.next.next
            else:
                aux = aux.next
        current_node = current_node.next
    linked_list.tail = aux
    return linked_list


