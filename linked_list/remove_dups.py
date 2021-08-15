from linked_list.linked_list import LinkedList


def remove_dups(linked_list: LinkedList) -> LinkedList:
    """
    Remove duplicates from an unsorted linked list.
    Reference: Cracking the Code Interview
    """
    visited_values = set()