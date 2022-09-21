
from dataclasses import dataclass
from typing import List, Any
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

        self.is_leafnode = False
    
    def __repr__(self) -> str:
        return f"{self.lower_bound}-{self.upper_bound}"
    
    def __eq__(self, other):
        return self.value == other.value

class LeafNode(Node):

    def __init__(self, lower_bound, upper_bound) -> None:
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.hash = md5()

        self.is_leafnode = True

    def in_leafnode(self, id):
        return self.lower_bound >= id < self.upper_bound

    def add_row(self, row):
        self.hash.update(row.value.encode())

    @property
    def value(self):
        return self.hash.hexdigest()
    
    def __repr__(self) -> str:
        return f"{self.lower_bound}-{self.upper_bound}: {self.value}"

class Partitioner:

    def __init__(self, min_id, max_id, nr_buckets) -> None:
        self.min_id = min_id
        self.max_id = max_id
        self.nr_buckets = nr_buckets

    def add_rows(self, rows: List[Row]):
        bucket_size = (self.max_id-self.min_id)/self.nr_buckets

        leafnodes = []
        for i in range(self.nr_buckets):
            bucket_min_id = self.min_id + int(i*bucket_size)
            bucket_max_id = bucket_min_id + int(bucket_size)
            leafnodes.append(LeafNode(bucket_min_id, bucket_max_id))

        for row in rows:
            for leafnode in leafnodes:
                if leafnode.in_leafnode(row.id):
                    leafnode.add_row(row)
        
        return leafnodes

class MerkleTree:

    def __init__(self, partitioner: Partitioner, data: List[Row]) -> None:
        self.tree = self._construct_tree(partitioner.add_rows(data))
    
    def _construct_tree(self, nodes: List[Node]):
        if len(nodes) > 1:
            parent_nodes = []
            for i in range(0, len(nodes), 2):
                left = nodes[i]
                right = nodes[i+1]
                
                parent_nodes.append(Node(left, right))

            return self._construct_tree(parent_nodes)
        return nodes[0]

    def compare_tree(self, tree: Any):
        self._compare_nodes(self.tree, tree)

    def _compare_nodes(self, left_node, right_node):
        if left_node != right_node:
            print(f"{left_node} != {right_node}")

            if not left_node.is_leafnode:
                self._compare_nodes(left_node._left, right_node._left)
                self._compare_nodes(left_node._right, right_node._right)

        else:
            print(f"{left_node} == {right_node}")

    def __repr__(self) -> str:
        return str(self.tree)

