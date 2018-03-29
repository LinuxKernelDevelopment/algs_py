#!/home/hmsjwzb/python/bin/python3

import math
from EdgeWeightedDigraph import EdgeWeightedDigraph
from EdgeWeightedDirectedCycle import EdgeWeightedDirectedCycle
from DirectedEdge import DirectedEdge
from DirectedCycle import DirectedCycle
from In import In
import sys
from queue import Queue

class BellmanFordSP:
    def __init__(self, G, s):
        self.distTo = [None] * G.Vertex()
        self.edgeTo = [None] * G.Vertex()
        self.onQueue = [None] * G.Vertex()
        self.cycle = []
        self.cost = 0
        for v in range(0, G.Vertex()):
            self.distTo[v] = math.inf
        self.distTo[s] = 0.0

        self.queue = Queue()
        self.queue.put(s)
        while not self.queue.empty() and not self.hasNegativeCycle():
            v = self.queue.get()
            self.onQueue[v] = False
            self.relax(G, v)
        assert(self.check(G, s))

    def relax(self, G, v):
        for e in G.adj[v]:
            w = e.eto()
            if self.distTo[w] > self.distTo[v] + e.Weight():
                self.distTo[w] = self.distTo[v] + e.Weight()
                self.edgeTo[w] = e
                if not self.onQueue[w]:
                    self.queue.put(w)
                    self.onQueue[w] = True
            if self.cost % G.Vertex() == 0:
                self.cost += 1
                self.findNegativeCycle()
                if self.hasNegativeCycle():
                    return

    def hasNegativeCycle(self):
        return self.cycle != []

    def negativeCycle(self):
        return self.cycle

    def findNegativeCycle(self):
        V = len(self.edgeTo)
        spt = EdgeWeightedDigraph(V, None, None)
        for v in range(0, V):
            if self.edgeTo[v] != None:
                spt.addEdge(self.edgeTo[v])

        finder = EdgeWeightedDirectedCycle(spt)
        self.cycle = finder.cycle

    def DistTo(self, v):
        self.validateVertex(v)
        if self.hasNegativeCycle():
            raise ValueError("Negative cost cycle exists")
        return self.distTo[v]

    def hasPathTo(self, v):
        self.validateVertex(v)
        return self.distTo[v] < math.inf

    def pathTo(self, v):
        self.validateVertex(v)
        if self.hasNegativeCycle():
            raise ValueError("Negative cost cycle exits")
        if not self.hasPathTo(v):
            return None
        path = []
        e = self.edgeTo[v]
        while e != None:
            path += [e]
            e = self.edgeTo[e.efrom()]
        return path

    def check(self, G, s):
        if self.hasNegativeCycle():
            weight = 0.0
            for e in self.negativeCycle():
                weight += e.weight()
            if weight >= 0.0:
                print("error: weight of negative cycle = " + weight)
                return False
        else:
            if self.distTo[s] != 0.0 or self.edgeTo[s] != None:
                print("distanceTo[s] and edgeTo[s] inconsistent")
                return False
            
            for v in range(0, G.Vertex()):
                if v == s:
                    continue
                if self.edgeTo[v] == None and self.distTo[v] == math.inf:
                    print("distTo[] and edgeTo[] inconsistent")
                    return False

            for v in range(0, G.Vertex()):
                for e in G.adj[v]:
                    w = e.eto()
                    if self.distTo[v] + e.Weight() < self.distTo[w]:
                        print("edge " + e + " not relaxed")
                        return False

            for w in range(0, G.Vertex()):
                if self.edgeTo[w] == None:
                    continue
                e = self.edgeTo[w]
                v = e.efrom()
                if w != e.eto():
                    return False
                if self.distTo[v] + e.Weight() != self.distTo[w]:
                    print("edge " + e + " on shortest path not tight")
                    return False

            print("Satisfies optimality conditions")
            print("\n")
            return True

    def validateVertex(self, v):
        V = len(self.distTo)
        if v < 0 or v >= V:
            raise ValueError("vertex " + v + " is not between 0 and " + (V-1))

if __name__ == '__main__':
    tmpstr = ""
    myin = In(sys.argv[1], None)
    s = int(sys.argv[2])
    G = EdgeWeightedDigraph(myin, None, None)

    sp = BellmanFordSP(G, s)

    if sp.hasNegativeCycle():
        for e in sp.negativeCycle():
            print(e)
    else:
        for v in range(0, G.Vertex()):
            if sp.hasPathTo(v):
                print("%d to %d (%5.2f) " % (s, v, sp.DistTo(v)))
                for e in sp.pathTo(v):
                    tmpstr += str(e) + "  "
                print(tmpstr)
                tmpstr = ""
                print("\n")
            else:
                print("%d to %d    no path\n" % (s, v))



