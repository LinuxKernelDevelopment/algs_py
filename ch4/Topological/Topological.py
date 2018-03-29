#!/home/hmsjwzb/python/bin/python3.5

import sys
from DirectedCycle import DirectedCycle
from DepthFirstOrder import DepthFirstOrder
from SymbolDigraph import SymbolDigraph

class Topological:
    def __init__(self, G):
        finder = DirectedCycle(G)
        if not finder.hasCycle():
            dfs = DepthFirstOrder(G)
            self.order = dfs.reversePost()
            self.rank = [0] * G.Vertex()
            i = 0
            for v in self.order:
                i += 1
                self.rank[v] = i

    def Order(self):
        return self.order

    def hasOrder(self):
        return self.order != None

    def isDAG(self):
        return self.hasOrder()

    def Rank(self, v):
        self.validateVertex(v)
        if self.hasOrder():
            return self.rank[v]
        else:
            return -1

    def validateVertex(self, v):
        V = len(self.rank)
        if v < 0 or v >= V:
            raise("vertex %d is not between 0 and %d " % (v, V-1))

if __name__ == '__main__':
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    sg = SymbolDigraph(filename, delimiter)
    topological = Topological(sg.digraph())
    for v in topological.Order():
        print(sg.nameOf(v))
