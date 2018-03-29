#!/home/hmsjwzb/python/bin/python3

from In import In
import sys
import math
from Topological import Topological
from EdgeWeightedDigraph import EdgeWeightedDigraph

class AcyclicSP:
    def __init__(self, G, s):
        self.distTo = [math.inf] * G.Vertex()
        self.edgeTo = [None] * G.Vertex()

        self.validateVertex(s)

        for v in range(0, G.Vertex()):
            self.distTo[v] = math.inf
        self.distTo[s] = 0.0

        topological = Topological(G)
        print(topological.Order())
        if not topological.hasOrder():
            raise ValueError("Digraph is not acyclic.")
        for v in topological.Order():
            for e in G.adj[v]:
                self.relax(e)

    def relax(self, e):
        v = e.efrom()
        w = e.eto()
        if self.distTo[w] > self.distTo[v] + e.weight:
            self.distTo[w] = self.distTo[v] + e.weight
            self.edgeTo[w] = e

    def DistTo(self, v):
        self.validateVertex(v)
        return self.distTo[v]

    def hasPathTo(self, v):
        self.validateVertex(v)
        return self.distTo[v] < math.inf

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

    def validateVertex(self, v):
        V = len(self.distTo)
        if v < 0 or v >= V:
            raise ValueError("vertex %d is not between 0 and %d " % (v, V-1))


if __name__ == '__main__':
    myin = In(sys.argv[1], None)
    s = int(sys.argv[2])
    G = EdgeWeightedDigraph(myin, None, None)

    sp = AcyclicSP(G, s)
    for v in range(0, G.Vertex()):
        tmpstr = ""
        if sp.hasPathTo(v):
            print("%d to %d (%.2f) " % (s, v, sp.DistTo(v)))
            for e in sp.pathTo(v):
                tmpstr += str(e) + " "
            print(tmpstr)
            print("\n")
        else:
            print("%d to %d  no path" % (s, v))
