#!/home/hmsjwzb/python/bin/python3

from In import In
import sys
from DirectedEdge import DirectedEdge
from EdgeWeightedDigraph import EdgeWeightedDigraph
from IndexMinPQ import IndexMinPQ
import math

class DijkstraSP:
    def __init__(self, G, s):
        for e in G.edges():
            if e.eweight() < 0:
                raise ValueError("edge " + e + " has negative weight")

        self.distTo = [0.0] * G.Vertex()
        self.edgeTo = [None] * G.Vertex()
        self.pq = IndexMinPQ(G.Vertex() + 1)

        self.validateVertex(s)

        for v in range(0, G.Vertex()):
            self.distTo[v] = math.inf
        self.distTo[s] = 0.0
        self.pq.insert(s, self.distTo[s])
        while not self.pq.isEmpty():
            v = self.pq.delMin()
            for e in G.adj[v]:
                self.relax(e)

        self.check(G)

    def relax(self, e):
        v = e.efrom()
        w = e.eto()
        if self.distTo[w] > self.distTo[v] + e.eweight():
            self.distTo[w] = self.distTo[v] + e.eweight()
            self.edgeTo[w] = e
            if self.pq.contains(w):
                self.pq.descreaseKey(w, self.distTo[w])
            else:
                self.pq.insert(w, self.distTo[w])

    def hasPathTo(self, v):
        self.validateVertex(v)
        return self.distTo[v]

    def pathTo(self, v):
        self.validateVertex(v)
        if not self.hasPathTo(v):
            return None
        path = []
        e = self.edgeTo[v]
        while e != None:
            path += [e]
            e = self.edgeTo[e.efrom()]
        return path

    def check(G, s):
        pass

    def validateVertex(self, v):
        V = len(self.distTo)
        if v < 0 or v >= V:
            raise ValueError("vertex " + str(v) + " is not between 0 and " + str(V-1))

if __name__ == '__main__':
    myin = In(sys.argv[1], None)
    G = EdgeWeightedDigraph(myin, None, None)
    s = int(sys.argv[2])

    sp = DijkstraSP(G, s)

    for t in range(0, G.Vertex()):
        if sp.hasPathTo(t):
            print("%d to %d (%.2f)  " % (s, t, sp.distTo[t]))
            for e in sp.pathTo(t):
                print(e)
            print("\n")
        else:
            print("%d to %d      no path\n" % (s, t))
