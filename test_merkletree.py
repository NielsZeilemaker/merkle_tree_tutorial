from random import sample, choices
from string import ascii_lowercase
from solution.merkletree import MerkleTree, Row

def test_tree():
    rows = [Row(id, ''.join(choices(ascii_lowercase))) for id in sample(range(10000000), k=8)]
    
    t = MerkleTree(rows)
    t.get_tree()
