from src.linked_list.linked_list import LinkedList


def sum_lists(linked_list1: LinkedList, linked_list2: LinkedList) -> LinkedList:
    """
    You have two numbers represented by a linked list, where each node contains a single
    digit. The digits are stored in reverse order, such that the 1 's digit is at the
    head of the list. Implements a function that adds the two numbers and returns the sum
    as a linked list.

    Input: (7->  1  -> 6)  + (5  ->  9  ->  2). That is, 617  +  295.
    Output: 2  ->  1  ->  9. That is, 912.

    """

    result_linked_list = LinkedList()
    current_node1, current_node2 = linked_list1.head, linked_list2.head
    carry = 0

    while current_node1 or current_node2:
        result = 0
        if current_node1:
            result += current_node1.item
            current_node1 = current_node1.next

        if current_node2:
            result += current_node2.item
            current_node2 = current_node2.next

        result += carry

        carry = result // 10
        result_linked_list.push_back(result % 10)

    if carry:
        result_linked_list.push_back(carry)

    return result_linked_list
