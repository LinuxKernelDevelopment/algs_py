#!/home/hmsjwzb/python/bin/python3.5
from In import In
import sys
from Edge import Edge
from EdgeWeightedGraph import EdgeWeightedGraph
from MinPQ import MinPQ
from UF import UF

class KruskalMST:
    def __init__(self, G):
        self.mst = []
        self.weight = 0.0
        pq = MinPQ()
        for e in G.edges():
            pq.insert(e)

        uf = UF(G.Vertex())
        while not pq.isEmpty() and len(self.mst) < G.Vertex() - 1:
            e = pq.delMin()
            v = e.either()
            w = e.other(v)
            if not uf.connected(v, w):
                uf.union(v, w)
                self.mst += [e]
                self.weight += e.weight

        self.check(G)

    def edges(self):
        return self.mst

    def weight(self):
        return self.weight

    def check(self, G):
        pass

if __name__ == '__main__':
    myin = In(sys.argv[1], None)
    G = EdgeWeightedGraph(myin)
    mst = KruskalMST(G)
    for e in mst.edges():
        print(e)
    print("%.5f\n" % mst.weight)
