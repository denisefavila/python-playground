from typing import List, Any

import pytest

from src.linked_list.linked_list import LinkedListWithoutTail, LinkedListWithTail
from src.linked_list.remove_duplicates import remove_duplicates


class TestLinkedList:

    @pytest.fixture
    def linked_list_without_tail(self, request) -> LinkedListWithoutTail:
        values = request.param
        linked_list = LinkedListWithoutTail()
        for value in values:
            linked_list.push_back(value)
        return linked_list

    @pytest.fixture
    def linked_list_with_tail(self, request) -> LinkedListWithTail:
        values = request.param
        linked_list = LinkedListWithTail()
        for value in values:
            linked_list.push_back(value)
        return linked_list

    @pytest.mark.parametrize(
        'linked_list_with_tail, expected_final_items',
        [
            ([1, 2, 3], [1, 2, 3]),
            ([], []),
            ([1, 2, 2], [1, 2])
        ],
        indirect=['linked_list_with_tail'])
    def test_remove_duplicates_with_tail(
            self,
            linked_list_with_tail,
            expected_final_items
    ):

        resultant_linked_list = remove_duplicates(linked_list_with_tail)
        assert resultant_linked_list.items() == expected_final_items

    @pytest.mark.parametrize(
        'linked_list_without_tail, expected_final_items',
        [
            ([1, 2, 3], [1, 2, 3]),
            ([], []),
            ([1, 2, 2], [1, 2]),
            ([1, 1, 2], [1, 2])
        ],
        indirect=['linked_list_without_tail'])
    def test_remove_duplicates_without_tail(
            self,
            linked_list_without_tail,
            expected_final_items
    ):

        resultant_linked_list = remove_duplicates(linked_list_without_tail)
        assert resultant_linked_list.items() == expected_final_items
