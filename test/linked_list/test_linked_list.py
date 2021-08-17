import pytest

from src.linked_list.k_to_last import remove_kth_to_last
from src.linked_list.node import Node
from src.linked_list.remove_duplicates import remove_duplicates, distinct_elements
from src.linked_list.reverse import reverse
from src.linked_list.swap_nodes_in_pair import swap_pairs


class TestLinkedList:

    @pytest.fixture
    def linked_list(self, request) -> Node:
        values = request.param

        if not values:
            return

        head = Node(item=values[0])

        last_node = head
        for value in values[1:]:
            new_node = Node(item=value)
            while last_node.next:
                last_node = last_node.next

            last_node.next = new_node
        return head

    @pytest.mark.parametrize(
        'linked_list, expected_final_items',
        [
            ([1, 2, 3], [1, 2, 3]),
            ([1, 2, 2], [1, 2]),
            ([1, 1, 2], [1, 2]),
            (['a', 'b', 'c', 'c'], ['a', 'b', 'c']),
            ([], [])
        ],
        indirect=['linked_list'])
    def test_remove_duplicates(
            self,
            linked_list,
            expected_final_items,
    ):
        result = remove_duplicates(linked_list)

        items = []
        current = result
        while current:
            items.append(current.item)
            current = current.next

        assert items == expected_final_items

    @pytest.mark.parametrize(
        'linked_list, expected_final_items',
        [
            ([1, 2, 3], [1, 2, 3]),
            ([1, 2, 2], [1]),
            ([1, 1, 2], [2]),
            (['a', 'b', 'c', 'c'], ['a', 'b']),
            ([], [])
        ],
        indirect=['linked_list'])
    def test_distinct_elements(
            self,
            linked_list,
            expected_final_items,
    ):
        result = distinct_elements(linked_list)

        items = []
        current = result
        while current:
            items.append(current.item)
            current = current.next

        assert items == expected_final_items

    @pytest.mark.parametrize(
        'linked_list, expected_final_items',
        [
            ([1, 2, 3], [3, 2, 1]),
            ([1, 2, 2], [2, 2, 1]),
            ([1, 1, 2], [2, 1, 1]),
            (['a', 'b', 'c', 'c'], ['c', 'c', 'b', 'a']),
            ([], [])
        ],
        indirect=['linked_list'])
    def test_reverse(
            self,
            linked_list,
            expected_final_items,
    ):
        result = reverse(linked_list)

        items = []
        current = result
        while current:
            items.append(current.item)
            current = current.next

        assert items == expected_final_items

    @pytest.mark.parametrize(
        'linked_list, expected_final_items, k',
        [
            ([1, 2, 3, 4], [1, 2, 4], 2),
            ([1, 2, 2], [1, 2], 1),
            ([1, 1, 2], [1, 2], 3),
            ([], [], 2),
            ([1, 2, 3, 4], [1, 2, 3, 4], 6),
        ],
        indirect=['linked_list'])
    def test_remove_k_to_last(
            self,
            linked_list,
            expected_final_items,
            k
    ):
        result = remove_kth_to_last(linked_list, k)

        items = []
        current = result
        while current:
            items.append(current.item)
            current = current.next

        assert items == expected_final_items

    @pytest.mark.parametrize(
        'linked_list, expected_final_items',
        [
            ([1, 2, 3, 4], [2, 1, 4, 3]),
            ([1, 2, 2], [2, 1, 2]),
            ([1, 1, 2], [1, 1, 2]),
            ([], []),
        ],
        indirect=['linked_list'])
    def test_swap_pairs(
            self,
            linked_list,
            expected_final_items,
    ):
        result = swap_pairs(linked_list)

        items = []
        current = result
        while current:
            items.append(current.item)
            current = current.next

        assert items == expected_final_items
