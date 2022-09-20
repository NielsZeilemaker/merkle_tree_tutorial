
from dataclasses import dataclass
from typing import List
from heapq import heappush
from hashlib import md5


@dataclass(order=True)
class Row:
    id: int
    value: str

class Node:

    def __init__(self, left, right) -> None:
        self._left = left
        self._right = right

        self.lower_bound = left.lower_bound
        self.upper_bound = right.upper_bound
        self.value = md5(f"{left.value}{right.value}".encode()).hexdigest()
    
    def __repr__(self) -> str:
        return f"{self.lower_bound}-{self.upper_bound}"
    
class LeafNode(Node):

    def __init__(self, row: Row) -> None:
        self.lower_bound = row.id
        self.upper_bound = row.id
        self.value = md5(row.value.encode()).hexdigest()

class MerkleTree:

    def __init__(self, data: List[Row]) -> None:
        self.heap = []
        for row in data:
            self.add_row(row)
    
    def add_row(self, row: Row):
        heappush(self.heap, row)

    def get_tree(self):
        leaf_nodes = []
        for i in range(0, len(self.heap), 2):
            left = self.heap[i]
            right = self.heap[i+1]
            
            leaf_nodes.append(Node(
                LeafNode(left),
                LeafNode(right)
                ))

        return self._construct_tree(leaf_nodes)

    def _construct_tree(self, nodes: List[Node]):
        if len(nodes) > 1:
            parent_nodes = []
            for i in range(0, len(nodes), 2):
                left = nodes[i]
                right = nodes[i+1]
                
                parent_nodes.append(Node(left, right))

            return self._construct_tree(parent_nodes)
        return nodes

