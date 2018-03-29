#!/home/hmsjwzb/python/bin/python3

from In import In
import sys
from Edge import Edge
from EdgeWeightedGraph import EdgeWeightedGraph
from IndexMinPQ import IndexMinPQ

class PrimMST:
    def __init__(self, G):
        self.edgeTo = [None] * G.Vertex()
        self.distTo = [None] * G.Vertex()
        self.marked = [False] * G.Vertex()
        self.pq = IndexMinPQ(G.Vertex())
        for v in range(0, G.Vertex()):
            self.distTo[v] = float('inf')
        for v in range(0, G.Vertex()):
            if not self.marked[v]:
                self.prim(G, v)

        #assert(self.check(G))

    def prim(self, G, s):
        self.distTo[s] = 0.0
        self.pq.insert(s, self.distTo[s])
        while not self.pq.isEmpty():
            v = self.pq.delMin()
            self.scan(G, v)

    def scan(self, G, v):
        self.marked[v] = True
        for e in G.adj[v]:
            w = e.other(v)
            if self.marked[w]:
                continue
            if e.Weight() <self.distTo[w]:
                self.distTo[w] = e.Weight()
                self.edgeTo[w] = e
                if self.pq.contains(w):
                    self.pq.decreaseKey(w, self.distTo[w])
                else:
                    self.pq.insert(w, self.distTo[w])

    def edges(self):
        mst = []
        for v in range(0, len(self.edgeTo)):
            e = self.edgeTo[v]
            if e != None:
                mst += [e]
        return mst

    def weight(self):
        weight = 0.0
        for e in self.edges():
            weight += e.Weight()
        return weight

    def check(self, G):
        pass

if __name__ == '__main__':
    myin = In(sys.argv[1], None)
    G = EdgeWeightedGraph(myin)
    mst = PrimMST(G)
    for e in mst.edges():
        print(e)
    print("%.5f\n" % mst.weight())

