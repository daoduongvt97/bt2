class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
class PrefixCodeTree(Node):
    def __init__(self):
        self.root = None
    def addNodeLeft(self,parent, val):
        parent.l = Node(val)
    def addNodeRight(self,parent, val):
        parent.r = Node(val)
    def insert(self,codeword, symbol):
        if(self.root == None):
            self.root = Node('')
        nodeTemp = self.root
        for ele in codeword:
            if(ele == 0):
                nodeTemp.l = Node(nodeTemp.l.v)
                nodeTemp = nodeTemp.l
            else:
                nodeTemp.r = Node(nodeTemp.r.v)
                nodeTemp = nodeTemp.r
        nodeTemp.v = symbol
    def decode(self, encodeedData, datalen):
        data = encodeedData.split()
        for i in range (0,datalen):

Tree = PrefixCodeTree()
