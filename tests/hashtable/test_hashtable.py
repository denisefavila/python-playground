from typing import Tuple, Hashable

import pytest

from hash_table.hash_table import Hashtable, Node


class TestHashTable:

    common_args = ('idx, key', [[0, 'bla'], [0, 'blabla']])

    @pytest.fixture
    def empty_hashtable(self) -> Hashtable:
        return Hashtable(size=3)

    @pytest.fixture
    def filled_hashtable(self, idx: int, key: Hashable) -> Hashtable:
        hashtable = Hashtable(size=3)
        hashtable.buckets[idx] = Node(key=key, value=10)

        return hashtable

    def test_get_item_key_error(self, empty_hashtable: Hashtable):
        with pytest.raises(KeyError):
            _ = empty_hashtable['bla']

    def test_set_item_without_collision(self, empty_hashtable: Hashtable) -> None:

        key = 'key'
        expected_idx = hash(key) % empty_hashtable.size
        assert not empty_hashtable.buckets[expected_idx]

        empty_hashtable[key] = 10
        expected_node = empty_hashtable.buckets[expected_idx]
        assert expected_node.key == key
        assert expected_node.value == 10
        assert not expected_node.next
