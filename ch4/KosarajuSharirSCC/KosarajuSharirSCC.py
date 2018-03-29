#!/home/hmsjwzb/python/bin/python3.5
import sys
from DepthFirstOrder import DepthFirstOrder
from In import In
from Digraph import Digraph

class KosarajuSharirSCC:
    def __init__(self, G):
        dfs = DepthFirstOrder(G.reverse())
        self.marked = [False] * G.Vertex()
        self.id = [0] * G.Vertex()
        self.count = 0
        for v in dfs.reversePost():
            if not self.marked[v]:
                self.dfs(G, v)
                self.count += 1

    def dfs(self, G, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)

    def mcount(self):
        return self.count

    def stronglyConnected(self, v, w):
        self.validateVertex(v)
        self.validateVertex(w)
        return self.id[v] == self.id[w]

    def vid(self, v):
        self.validateVertex(v)
        return self.id[v]

    def check(self, G):
        pass

    def validateVertex(self, v):
        V = len(self.marked)
        if v < 0 or v >= V:
            raise("vertex %d is not between 0 and %d" % (v, V-1))

if __name__ == '__main__':
    myin = In(sys.argv[1], None)
    G = Digraph(myin)
    scc = KosarajuSharirSCC(G)
    m = scc.mcount()
    print("%d strong components" % m)

    components = [None] * m
    for i in range(0, m):
        components[i] = []
    for v in range(0, G.Vertex()):
        components[scc.vid(v)].append(v)

    s = ""
    for i in range(0, m):
        for v in components[i]:
            s += "%d " % v
        s += '\n'
    print(s)
