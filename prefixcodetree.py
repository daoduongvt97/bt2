class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.isLeaf = True
class PrefixCodeTree(Node):
    def __init__(self):
        self.root = None
    def insert(self,codeword, symbol):
        if(self.root == None):
            self.root = Node('')
        nodeTemp = self.root
        for ele in codeword:
            if(ele == 0):
                if(nodeTemp.l == None):
                    nodeTemp.l = Node('')
                nodeTemp.isLeaf = False
                nodeTemp = nodeTemp.l
            else:
                if(nodeTemp.r == None):
                    nodeTemp.r = Node('')
                nodeTemp.isLeaf = False
                nodeTemp = nodeTemp.r
            nodeTemp.v = symbol
    def getData(self,root, code):
      return root.l if(code == '0') else root.r
    def decode(self, encodeedData, datalen):
        encodeedData = int.from_bytes(encodeedData, byteorder='big')
        encodeedData = (bin(encodeedData)[2:])
        result = []
        nodeTemp = self.root
        i = 0
        while(i <= datalen):
            if(nodeTemp.isLeaf == True):
                result.append(nodeTemp.v)
                nodeTemp = self.root
                i = i-1
            else:
                nodeTemp = self.getData(nodeTemp, encodeedData[i])
            i = i +1
        return ''.join(result)