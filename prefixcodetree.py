class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
class PrefixCodeTree:
    def __init__(self):
        self.root = None
    def __index__(self, root):
        self.root = root
    def insert(codeword, symbol):
