#!/home/hmsjwzb/python/bin/python3
from Digraph import Digraph
import sys
from In import In

class DirectedDFS:
    def __init__(self, *args):
        if type(args[0]) is int:
            self.DirectedDFS_digraph(args[0], args[1])
        else:
            self.DirectedDFS_iterable(args[0], args[1])

    def DirectedDFS_digraph(self, G, s):
        self.count = 0
        self.marked = [False] * G.Vertex()
        self.validateVertex(s)
        self.dfs(G, s)

    def DirectedDFS_iterable(self, G, sources):
        self.count = 0
        self.marked = [False] * G.Vertex()
        self.validateVertices(sources)
        for v in sources:
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G, v):
        self.count += 1
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)

    def marked(self, v):
        self.validateVertex(v)
        return self.marked[v]

    def count(self):
        return self.count

    def validateVertex(self, v):
        V = len(self.marked)
        if v < 0 or v >= V:
            raise Exception("vertex %d is not between 0 and %d \n" % (v, (V-1)))

    def validateVertices(self, vertices):
        if vertices == None:
            raise Exception("argument is None")
        V = len(self.marked)
        for v in vertices:
            if v < 0 or v >= V:
                raise Exception("vertex %d is not between 0 and %d \n" % (v, (V-1)))


if __name__ == '__main__':
    myin = In(sys.argv[1])
    G = Digraph(myin)

    sources = []
    for s in sys.argv[2:]:
        sources.append(int(s))

    dfs = DirectedDFS(G, sources)

    s = ""
    for v in range(0, G.Vertex()):
        if dfs.marked[v]:
            s += "%d " % v
    print(s)
            
