from linked_list.linked_list import LinkedList


def remove_dups(linked_list: LinkedList) -> LinkedList:
    """
    Remove duplicates from an unsorted linked list.
    """
    visited_values = set()