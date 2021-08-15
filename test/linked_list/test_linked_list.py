import pytest

from src.linked_list.with_tail.k_to_last import kth_to_last
from src.linked_list.with_tail.linked_list import LinkedListWithTail
from src.linked_list.with_tail.remove_duplicates import remove_duplicates_without_buffer
from src.linked_list.without_tail.linked_list import LinkedListWithoutTail
from src.linked_list.without_tail.remove_duplicates import remove_duplicates


class TestLinkedListWithoutTail:

    @pytest.fixture
    def linked_list_without_tail(self, request) -> LinkedListWithoutTail:
        values = request.param
        linked_list = LinkedListWithoutTail()
        for value in values:
            linked_list.push_back(value)
        return linked_list

    @pytest.mark.parametrize(
        'linked_list_without_tail, expected_final_items, head',
        [
            ([1, 2, 3], [1, 2, 3], 1),
            ([1, 2, 2], [1, 2], 1),
            ([1, 1, 2], [1, 2], 1)
        ],
        indirect=['linked_list_without_tail'])
    def test_remove_duplicates(
            self,
            linked_list_without_tail,
            expected_final_items,
            head,
    ):

        resultant_linked_list = remove_duplicates(linked_list_without_tail)
        assert resultant_linked_list.items() == expected_final_items
        assert resultant_linked_list.head.item == head

    @pytest.mark.parametrize(
        'linked_list_without_tail, expected_final_items, head',
        [
            ([], [], None),
        ],
        indirect=['linked_list_without_tail'])
    def test_remove_duplicates_empty(
            self,
            linked_list_without_tail,
            expected_final_items,
            head,
    ):

        resultant_linked_list = remove_duplicates(linked_list_without_tail)
        assert resultant_linked_list.items() == expected_final_items
        assert resultant_linked_list.head == head


class TestLinkedListWithTail:

    @pytest.fixture
    def linked_list_with_tail(self, request) -> LinkedListWithTail:
        values = request.param
        linked_list = LinkedListWithTail()
        for value in values:
            linked_list.push_back(value)
        return linked_list

    @pytest.mark.parametrize(
        'linked_list_with_tail, expected_final_items, head, tail',
        [
            ([1, 2, 3], [1, 2, 3], 1, 3),
            ([1, 2, 2], [1, 2], 1, 2),
            ([1, 1, 2], [1, 2], 1, 2)
        ],
        indirect=['linked_list_with_tail'])
    def test_remove_duplicates(
            self,
            linked_list_with_tail,
            expected_final_items,
            head,
            tail
    ):

        resultant_linked_list = remove_duplicates(linked_list_with_tail)
        assert resultant_linked_list.items() == expected_final_items
        assert resultant_linked_list.head.item == head
        assert resultant_linked_list.tail.item == tail

    @pytest.mark.parametrize(
        'linked_list_with_tail, expected_final_items, head, tail',
        [
            ([1, 2, 3], [1, 2, 3], 1, 3),
            ([1, 2, 2], [1, 2], 1, 2),
            ([1, 1, 2], [1, 2], 1, 2)
        ],
        indirect=['linked_list_with_tail'])
    def test_remove_duplicates_without_buffer(
            self,
            linked_list_with_tail,
            expected_final_items,
            head,
            tail
    ):
        resultant_linked_list = remove_duplicates_without_buffer(linked_list_with_tail)
        assert resultant_linked_list.items() == expected_final_items
        assert resultant_linked_list.head.item == head
        assert resultant_linked_list.tail.item == tail

    @pytest.mark.parametrize(
        'linked_list_with_tail, expected_final_items, head, tail',
        [
            ([], [], None, None),
        ],
        indirect=['linked_list_with_tail'])
    def test_remove_duplicates_empty(
            self,
            linked_list_with_tail,
            expected_final_items,
            head,
            tail
    ):

        resultant_linked_list = remove_duplicates(linked_list_with_tail)
        assert resultant_linked_list.items() == expected_final_items
        assert resultant_linked_list.head == head
        assert resultant_linked_list.tail == tail

    @pytest.mark.parametrize(
        'linked_list_with_tail, expected_final_items, head, tail',
        [
            ([], [], None, None),
        ],
        indirect=['linked_list_with_tail'])
    def test_remove_duplicates_without_buffer_empty(
            self,
            linked_list_with_tail,
            expected_final_items,
            head,
            tail
    ):
        resultant_linked_list = remove_duplicates_without_buffer(linked_list_with_tail)
        assert resultant_linked_list.items() == expected_final_items
        assert resultant_linked_list.head == head
        assert resultant_linked_list.tail == tail

    @pytest.mark.parametrize(
        'linked_list_with_tail, k, expected_item',
        [
            ([1, 2, 3], 1, 2),
            ([1, 2, 3, 4], 2, 2),
            ([1, 1, 2], 0, 2),
            ([1, 2], 3, None)
        ],
        indirect=['linked_list_with_tail'])
    def test_k_to_last(
            self,
            linked_list_with_tail,
            k,
            expected_item,
    ):
        result = kth_to_last(linked_list=linked_list_with_tail, k=k)
        assert result == expected_item
