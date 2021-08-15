from __future__ import annotations

from typing import Any, Protocol, List


class LinkedList(Protocol):
    """
        Implement the linked list interface.
    """

    def push_front(self, item: Any) -> None:
        """
        Inserts an item at the beginning.
        """

    def push_back(self, item: Any) -> None:
        """
        Inserts an item at the end.
        """

    def pop_front(self) -> None:
        """
        Removes an item at the beginning.
        """

    def pop_back(self) -> None:
        """
        Removes an item at the end.
        """

    def items(self) -> List[Any]:
        """
        Return items in Linked List.
        """
