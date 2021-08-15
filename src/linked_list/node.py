from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Union


@dataclass
class Node:
    item: Any
    next: Union[Node, None] = None

    def __repr__(self) -> str:
        return str(self.item)
