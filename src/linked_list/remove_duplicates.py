from typing import Optional

from src.linked_list.node import Node


def remove_duplicates(head: Optional[Node]) -> Optional[Node]:
    """
    Remove duplicates from an sorted linked list,
    such that each element appears only once.
    https://leetcode.com/problems/remove-duplicates-from-sorted-list/
    """

    current_node = head
    while current_node and current_node.next:
        if current_node.item == current_node.next.item:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
    return head


def distinct_elements(head: Optional[Node]) -> Optional[Node]:
    """
    Remove duplicates from an sorted linked list,
    leaving only distinct numbers from the original list. .
    https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
    """

    dummy = current_node = Node(item=0, next=head)

    while head:
        if head.next and head.item == head.next.item:
            # move till the end of duplicates
            while head.next and head.item == head.next.item:
                head = head.next
            current_node.next = head.next
        else:
            current_node = current_node.next

        head = head.next
    return dummy.next
