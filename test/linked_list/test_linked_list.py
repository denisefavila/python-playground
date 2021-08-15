import pytest

from src.linked_list.linked_list import LinkedList
from src.linked_list.remove_duplicates import remove_duplicates
from src.linked_list.reverse import reverse


class TestLinkedListWithoutTail:

    @pytest.fixture
    def linked_list(self, request) -> LinkedList:
        values = request.param
        linked_list = LinkedList()
        for value in values:
            linked_list.push_back(value)
        return linked_list

    @pytest.mark.parametrize(
        'linked_list, expected_final_items, head',
        [
            ([1, 2, 3], [1, 2, 3], 1),
            ([1, 2, 2], [1, 2], 1),
            ([1, 1, 2], [1, 2], 1)
        ],
        indirect=['linked_list'])
    def test_remove_duplicates(
            self,
            linked_list,
            expected_final_items,
            head,
    ):

        resultant_linked_list = remove_duplicates(linked_list)
        assert resultant_linked_list.items() == expected_final_items
        assert resultant_linked_list.head.item == head

    @pytest.mark.parametrize(
        'linked_list, expected_final_items, head',
        [
            ([], [], None),
        ],
        indirect=['linked_list'])
    def test_remove_duplicates_empty(
            self,
            linked_list,
            expected_final_items,
            head,
    ):

        resultant_linked_list = remove_duplicates(linked_list)
        assert resultant_linked_list.items() == expected_final_items
        assert resultant_linked_list.head == head

    @pytest.mark.parametrize(
        'linked_list, expected_final_items, head',
        [
            ([1, 2, 3], [3, 2, 1], 3),
            ([1, 2, 2], [2, 2, 1], 2),
            ([1, 1, 2], [2, 1, 1], 2),
            (['a', 'b', 'c', 'd'], ['d', 'c', 'b', 'a'], 'd')
        ],
        indirect=['linked_list'])
    def test_reverse_list(
            self,
            linked_list,
            expected_final_items,
            head,
    ):
        resultant_linked_list = reverse(linked_list)
        assert resultant_linked_list.items() == expected_final_items
        assert resultant_linked_list.head.item == head
