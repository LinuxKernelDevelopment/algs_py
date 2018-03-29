#!/home/hmsjwzb/python/bin/python3.5
import random
from In import In
import sys
from Edge import Edge

class EdgeWeightedGraph:
    def __init__(self, arg1, *therest):
        if type(arg1) is In:
            self.EdgeWeightedGraph_In(myin)
        else:
            self.EdgeWeightedGraph_Random_V(arg1, therest[0])

    def EdgeWeightedGraph_Empty_V(self, V):
        if V < 0:
            raise ValueError('Number of vertices must be nonnegative')
        self.V = V
        self.E = 0
        self.adj = [None] * V
        for v in range(0, V):
            self.adj[v] = []

    def EdgeWeightedGraph_Random_V(self, V, E):
        self.EdgeWeightedGraph_Empty_V(V)
        if E < 0:
            raise ValueError('Number of edges must be nonnegative')
        for i in range(0, E):
            v = random.randint(0, V-1)
            w = random.randint(0, V-1)
            weight = 100 * random.uniform(1, 10) / 100.0
            e = Edge(v, w, weight)
            self.addEdge(e)

    def EdgeWeightedGraph_In(self, myin):
        self.EdgeWeightedGraph_Empty_V(myin.readInt())
        self.E = myin.readInt()
        if self.E < 0:
            raise ValueError('Number of edges must be nonnegative')
        for i in range(0, self.E):
            v = myin.readInt()
            w = myin.readInt()
            self.validateVertex(v)
            self.validateVertex(w)
            weight = myin.readDouble()
            e = Edge(v, w, weight)
            self.addEdge(e)

    def EdgeWeightedGraph_Graph(self, G):
        self.EdgeWeightedGraph_Empty_V(G.Vertex())
        self.E = G.Edge()
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
            raise ValueError("vertex %d is not between 0 and %d " % (v, self.V-1))

    def addEdge(self, e):
        v = e.either()
        w = e.other(v)
        self.validateVertex(v)
        self.validateVertex(w)
        self.adj[v] += [e]
        self.adj[w] += [e]
        self.E += 1

    def adjacent(self, v):
        self.validateVertex(v)
        return self.adj[v]

    def degree(self, v):
        self.validateVertex(v)
        return self.adj[v].size()

    def edges(self):
        mylist = []
        for v in range(0, V):
            selfLoops = 0
            for e in self.adjacent(v):
                if e.other(v) > v:
                    mylist += [e]
                elif e.other(v) == v:
                    if selfLoops % 2 == 0:
                        mylist += [e]
                        selfLoops += 1
        return mylist

    def __str__(self):
        s = ""
        print(self.Vertex())
        print(self.Edge())
        s += "%d %d\n" % (self.Vertex(), self.Edge())
        for v in range(0, self.Vertex()):
            s += "%d:" % v
            for e in self.adj[v]:
                s += str(e) + "   "
            s += "\n"
        return s

if __name__ == '__main__':
    myin = In(sys.argv[1], None)
    #G = EdgeWeightedGraph(10, 10)
    G = EdgeWeightedGraph(myin)
    print(G)


