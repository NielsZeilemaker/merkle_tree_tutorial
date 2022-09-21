
from dataclasses import dataclass
from typing import List
from heapq import heappush


@dataclass(order=True)
class Row:
    id: int
    value: str


class MerkleTree:

    def __init__(self, partitioner: Partitioner, data: List[Row]) -> None:
        # exercise for the reader
        pass
    
    def compare_tree(self, tree):
        # exercise for the reader
        pass