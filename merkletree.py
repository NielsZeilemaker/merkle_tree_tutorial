
from dataclasses import dataclass
from typing import List
from heapq import heappush


@dataclass(order=True)
class Row:
    id: int
    value: str


class MerkleTree:

    def __init__(self, data: List[Row]) -> None:
        self.heap = []
        for row in data:
            self.add_row(row)
    
    def add_row(self, row: Row):
        heappush(self.heap, row)

    def get_tree(self):
        # exercise for the reader
        pass

    def compare_tree(self, tree):
        # exercise for the reader
        pass