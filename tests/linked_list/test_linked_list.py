import pytest

from linked_list.linked_list import LinkedList


class TestLinkedList:

    @pytest.fixture
    def linked_list_without_duplicates(self, values) -> LinkedList:
        linked_list = LinkedList()
        for value in values:
            linked_list.push_front(value)
        return linked_list

    def remove_duplicates_with_duplicates(self):
        pass

    def remove_duplicates_without_duplicates(self):
        pass