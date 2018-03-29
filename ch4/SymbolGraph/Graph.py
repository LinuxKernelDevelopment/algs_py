#!/home/hmsjwzb/python/bin/python3.5

from In import In
import sys

class Graph:
    def __init__(self, V):
        if type(V) is int:
            self.Graph_int_init(V)
        elif type(V) is In:
            self.Graph_input_init(V)
        elif type(V) is Graph:
            self.Graph_graph_init(V)

    def Graph_int_init(self, V):
        if V < 0:
            raise Exception("Number of vertices must be nonnegative")
        self.V = V
        self.E = 0
        self.adj = [None] * V
        for v in range(0, V):
            self.adj[v] = set()

    def Graph_input_init(self, stdin):
        self.V = stdin.readInt()
        if self.V < 0:
            raise Exception("number of vertices in a Graph must be nonnegative")
        self.adj = [None] * self.V
        for v in range(0, self.V):
            self.adj[v] = set()
        self.E = stdin.readInt()
        if self.E < 0:
            raise Exception("number of edges in a Graph must be nonnegative")
        for i in range(0, self.E):
            v = stdin.readInt()
            w = stdin.readInt()
            self.validateVertex(v)
            self.validateVertex(w)
            self.addEdge(v, w)

    def Graph_graph_init(self, G):
        self.__init__(G.Vertex())
        self.E = G.Edge()
        for v in range(0, G.Vertex()):
            reverse = []
            for w in G.adj[v]:
                reverse.add(w)
            for w in reverse:
                self.adj[v].add(w)

    def Vertex(self):
        return self.V

    def Edge(self):
        return self.E

    def validateVertex(self, v):
        if v < 0 or v >= self.V:
            raise Exception("vertex " + v + " is not between 0 and " + (self.V-1));

    def addEdge(self, v, w):
        self.validateVertex(v)
        self.validateVertex(w)
        self.E = self.E + 1
        self.adj[v].add(w)
        self.adj[w].add(v)

    def adj(self, v):
        self.validateVertex(v)
        return self.adj[v]

    def degree(self, v):
        self.validateVertex(v)
        return self.adj[v].size()

    def toString(self):
        s = ""
        s += "%d vertices, %d edges \n" % (self.V, self.E)
        for v in range(0, self.V):
            s += "%d: " % v
            for w in self.adj[v]:
                s += "%d " % w
            s += "\n"
        return s

if __name__ == '__main__':
    myin = In(sys.argv[1])
    G = Graph(myin)
    print(G.toString())
    N = Graph(G)
    print(N.toString())
