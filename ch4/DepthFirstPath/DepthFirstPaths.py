#!/home/hmsjwzb/python/bin/python3.5
import sys
from In import In
from Graph import Graph
class DepthFirstSearch:
    def __init__(self, G, s):
        self.s = s
        self.edgeTo = [None] * G.Vertex()
        self.marked = [None] * G.Vertex()
        self.count = 0
        self.dfs(G, s)

    def dfs(self, G, v):
        self.count += 1
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(G, w)

    def markedf(self, v):
        self.validateVertex(v)
        return self.marked[v]

    def countf(self):
        return self.count

    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, v):
        self.validateVertex(v)
        if not self.hasPahTo(v):
            return None
        path = []
        for x in self.edgeTo[x]:
            path.push(x)
        path.push(self.s)
        return path

    def validateVertex(self, v):
        V = len(self.marked)
        if v < 0 or v >= V:
            raise Exception("vertex " + v + " is not between 0 and " + (V-1))

if __name__ == '__main__':
    myin = In(sys.argv[1], None)
    G = Graph(myin)
    s = int(sys.argv[2])
    output = ""
    search = DepthFirstSearch(G, s)
    for v in range(0, G.Vertex()):
        if search.markedf(v):
            output += str(v)
            output += " "
    print(output)
    if search.countf() != G.Vertex():
        print("Not connected\n")
    else:
        print("connected\n")
