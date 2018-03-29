#!/home/hmsjwzb/python/bin/python3.5
import sys
from In import In
from math import inf
from Graph import Graph
from queue import Queue

class BreadthFirstPaths:
    def __init__(self, G, s):
        self.marked = [None] * G.Vertex()
        self.distTo = [None] * G.Vertex()
        self.edgeTo = [None] * G.Vertex()
        self.validateVertex(s)
        self.bfs(G, s)


    def bfs(self, G, s):
        q = Queue()
        for v in range(0, G.Vertex()):
            self.distTo[v] = inf
        self.distTo[s] = 0
        self.marked[s] = True
        q.put(s)

        while not q.empty():
            v = q.get()
            for w in G.adj[v]:
                if not self.marked[w]:
                    self.edgeTo[w] = v
                    self.distTo[w] = self.distTo[v] + 1
                    self.marked[w] = True
                    q.put(w)

    def hasPathTo(self, v):
        self.validateVertex(v)
        return self.marked[v]

    def distTo(self, v):
        self.validateVertex(v)
        return self.distTo[v]

    def pathTofun(self, v):
        self.validateVertex(v)
        path = []
        if not self.hasPathTo(v):
            return None
        x = v
        while self.distTo[x] != 0:
            path.append(x)
            x = self.edgeTo[x]
        path.append(x)
        return path

    def validateVertex(self, v):
        V = len(self.marked)
        if v < 0 or v >= V:
            raise Exception("vertex " + v + " is not between 0 and " + (V-1))

if __name__ == '__main__':
    myin = In(sys.argv[1])
    G = Graph(myin)

    s = int(sys.argv[2])
    bfs = BreadthFirstPaths(G, s)

    for v in range(0, G.Vertex()):
        rs = ""
        if bfs.hasPathTo(v):
            print("%d to %d (%d):  " % (s, v, bfs.distTo[v]))
            for x in bfs.pathTofun(v):
                if x == s: rs += str(x)
                else:      rs += str(x) + '-'
            print(rs + "\n")
        else:
            print("%d to %d (-): not connected\n" % (s, v))
