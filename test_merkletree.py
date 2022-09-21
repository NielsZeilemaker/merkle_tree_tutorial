from random import sample, choices
from string import ascii_lowercase
from solution.merkletree import MerkleTree, Partitioner, Row

def test_tree():
    partitioner = Partitioner(0, 10000000, 8)
    rows = [Row(id, ''.join(choices(ascii_lowercase))) for id in sample(range(10000000), k=1000)]
    
    t = MerkleTree(partitioner, rows)

def test_compare():
    partitioner = Partitioner(0, 8, 8)

    rows = [
        Row(1, "a"), 
        Row(2, "b"),
        Row(3, "a"),
        Row(4, "a"),
        Row(5, "a"),
        Row(6, "a"),
        Row(7, "a"),
        Row(8, "a")
    ]

    rows_small = rows[:1]
    
    t1 = MerkleTree(partitioner, rows)
    t2 = MerkleTree(partitioner, rows_small)

    t2.compare_tree(t1.tree)

    assert False