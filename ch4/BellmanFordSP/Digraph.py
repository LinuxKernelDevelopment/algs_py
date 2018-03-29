#!/home/hmsjwzb/python/bin/python3.5

from In import In
import sys

class Digraph:
    def __init__(self, V):
        if isinstance(V, int):
            self.empty_init(V)
        elif isinstance(V, Digraph):
            self.digraph_init(V)
        else:
            self.in_init(V)

    def empty_init(self, V):
        if V < 0:
            raise Exception("Number of vertices in Digraph must be nonnegative")
        self.V = V
        self.E = 0
        self.indegree = [0] * self.V
        self.adj = [None] * self.V
        for v in range(0, V):
            self.adj[v] = set()

    def in_init(self, myin):
        try:
            self.V = myin.readInt()
            print(self.V)
            if self.V < 0:
                raise Exception("number of vertices in a Digraph must be nonnegative")
            self.indegree = [0] * self.V
            self.adj = [None] * self.V
            for v in range(0, self.V):
                self.adj[v] = set()
            self.E = myin.readInt()
            if self.E < 0:
                raise Exception("number of edges in a Digraph must be nonnegative")
            for i in range(0, self.E):
                v = myin.readInt()
                w = myin.readInt()
                self.addEdge(v, w)
        except Exception:
            raise Exception("invalid input format in Digraph constructor")

    def digraph_init(self, G):
        self.__init__(G.Vertex())
        self.E = G.Edge()
        for v in range(0, G.Vertex()):
            reverse = []
            for w in G.adj[v]:
                reserse.append(w)
            reverse.reverse()
            for w in reverse:
                self.adj[v].add(w)

    def Vertex(self):
        return self.V

    def Edge(self):
        return self.E

    def validateVertex(self, v):
        if v < 0 or v >= self.V:
            raise Exception("vertex %d is not between 0 and %d" % (v, (V-1)))

    def addEdge(self, v, w):
        self.validateVertex(v)
        self.validateVertex(w)
        self.adj[v].add(w)
        self.indegree[w] += 1
        self.E += 1

    def outdegree(self, v):
        self.validateVertex(v)
        return len(self.adj[v])

    def indegree(self, v):
        self.validateVertex(v)
        return self.indegree[v]

    def reverse(self):
        reverse = Digraph(self.V)
        for v in range(0, self.V):
            for w in self.adj[v]:
                reverse.addEdge(w, v)
        return reverse

    def __str__(self):
        s = ""
        s += "%d vertices, %d edges\n" % (self.V, self.E)
        for v in range(0, self.V):
            s += "%d: " % v
            for w in self.adj[v]:
                s += "%d " % w
            s += '\n'
        return s

if __name__ == '__main__':
    myin = In(sys.argv[1], "\n")
    DG = Digraph(myin)
    print(DG)
    R = DG.reverse()
    print(R)

