#!/home/hmsjwzb/python/bin/python3.5
from MinPQ import MinPQ
from EdgeWeightedGraph import EdgeWeightedGraph
from In import In
import sys

class LazyPrimMST:
    def __init__(self, G):
        self.mst = []
        self.pq = MinPQ()
        self.marked = [False] * G.Vertex()
        self.Weight = 0
        for v in range(0, G.Vertex()):
            if not self.marked[v]:
                self.prim(G, v)
        #assert(self.check(G))

    def prim(self, G, s):
        self.scan(G, s)
        while not self.pq.isEmpty():
            e = self.pq.delMin()
            v = e.either()
            w = e.other(v)
            assert(self.marked[v] or self.marked[w])
            if self.marked[v] and self.marked[w]:
                continue
            self.mst += [e]
            self.Weight += e.weight
            if not self.marked[v]:
                self.scan(G, v)
            if not self.marked[w]:
                self.scan(G, w)
        
    def scan(self, G, v):
        assert(not self.marked[v])
        self.marked[v] = True
        for e in G.adj[v]:
            if not self.marked[e.other(v)]:
                self.pq.insert(e)

    def edges(self):
        return self.mst

    def weight(self):
        return self.Weight

    '''def check(self, G):
        totalWeight = 0.0
        for e in self.edges():
            totalWeight += e.weight()
        if abs(totalWeight - self.weight()) > pow(10, -12):
            print("Weight of edges does not equal weight(): %f vs. %f\n" % (totalWeight, self.weight()))
            return False
        uf = UF(G.V())
        for e in self.edges():
            v = e.either()
            w = e.other(v)
            if uf.connected(v, w):
                print("Not a forest")
                return False
            uf.union(v, w)

        for e in G.edges():
            v = e.either()
            w = e.other(v)
            if not uf.connected(v, w):
                print("Not a spanning forest")
                return False

        for e in self.edges():
            uf = UF(G.V())
            for f in self.mst:
                x = f.either()
                y = f.other(x)
                if f != e:
                    uf.union(x, y)

            for f in G.edges():
                x = f.either()
                y = f.other(x)
                if not uf.connected(x, y):
                    if f.weight() < e.weight():
                        print("Edge " + f + " violates cut optimality conditions")
                        return False
        return True'''

if __name__ == '__main__':
    myin = In(sys.argv[1], None)

    G = EdgeWeightedGraph(myin)
    mst = LazyPrimMST(G)
    for e in mst.edges():
        print(e)
    print("%5f\n" % mst.weight())
