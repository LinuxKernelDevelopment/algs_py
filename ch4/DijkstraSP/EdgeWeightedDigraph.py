#!/home/hmsjwzb/python/bin/python3
import sys
import os
import random
from DirectedEdge import DirectedEdge
from In import In

class EdgeWeightedDigraph:
    def __init__(self, arg1, arg2, arg3):
        if isinstance(arg1, int) and isinstance(arg2, int):
            self.EdgeWeightedDigraph_VE(arg1, arg2)
        elif isinstance(arg1, int):
            self.EdgeWeightedDigraph_Vertex(arg1)
        elif isinstance(arg1, EdgeWeightedDigraph):
            self.EdgeWeightedDigraph_G(arg1)
        else:
            self.EdgeWeightedDigraph_In(arg1)

    def EdgeWeightedDigraph_Vertex(self, V):
        if V < 0:
            raise ValueError("Number of vertices in Digraph must be nonnegative")
        self.V = V
        self.E = 0
        self.indegree = [0] * V
        self.adj = [None] * V
        for v in range(0, V):
            self.adj[v] = list()

    def EdgeWeightedDigraph_VE(self, V, E):
        self.EdgeWeightedDigraph_Vertex(V)
        if E < 0:
            raise ValueError("Number of edges in a Digraph must be nonnegative")
        for i in range(0, E):
            v = random.randint(0, V)
            w = random.randint(0, V)
            weight = 0.01 * random.uniform(0, 100)
            e = DirectedEdge(v, w, weight)
            self.addEdge(e)

    def EdgeWeightedDigraph_In(self, myin):
        self.__init__(myin.readInt(), None, None)
        E = myin.readInt()
        if E < 0:
            raise ValueError("Number of edges must be nonnegative")
        for i in range(0, E):
            v = myin.readInt()
            w = myin.readInt()
            self.validateVertex(v)
            self.validateVertex(w)
            weight = myin.readDouble()
            self.addEdge(DirectedEdge(v, w, weight))

    def EdgeWeightedDigraph_G(self, G):
        self.__init__(G.Vertex())
        self.E = G.Edge()
        for v in range(0, G.Vertex()):
            self.indegree[v] = G.indegree(v)
        for v in range(0, G.Vertex()):
            reverse = []
            for e in G.adj[v]:
                reverse += [e]
            for e in reverse:
                self.adj[v] += [e]

    def Vertex(self):
        return self.V

    def Edge(self):
        return self.E

    def validateVertex(self, v):
        if v < 0 or v >= self.V:
            raise ValueError("vertex " + v + " is not between 0 and " + (V-1))

    def addEdge(self, e):
        v = e.efrom()
        w = e.eto()
        self.validateVertex(v)
        self.validateVertex(w)
        self.adj[v] += [e]
        self.indegree[w] += 1
        self.E += 1

    def adj(self, v):
        self.validateVertex(v)
        return self.adj[v]

    def outdegree(self, v):
        self.validateVertex(v)
        return len(adj[v])

    def indegree(self, v):
        self.validateVertex(v)
        return self.indegree[v]

    def edges(self):
        tl = []
        for v in range(0, self.V):
            for e in self.adj[v]:
                tl += [e]
        return tl

    def toString(self):
        s = ""
        s += "%d %d\n" % (self.V, self.E)
        for v in range(0, self.V):
            s += "%d: " % v
            for e in self.adj[v]:
                s += str(e)
                s += " "
            s += "\n"
        return s

    def __str__(self):
        return self.toString()

if __name__ == '__main__':
    myin = In(sys.argv[1], None)
    G = EdgeWeightedDigraph(myin, None, None)
    print(G)
