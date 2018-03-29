#!/home/hmsjwzb/python/bin/python3.5
import sys
from In import In
from Graph import Graph
import queue

class CC:
    def __init__(self, G):
        self.marked = [None] * G.Vertex()
        self.cid = [None] * G.Vertex()
        self.size = [0] * G.Vertex()
        self.count = 0
        for v in range(0, G.Vertex()):
            if not self.marked[v]:
                self.dfs(G, v)
                self.count += 1

    def dfs(self, G, v):
        self.marked[v] = True
        self.cid[v] = self.count
        self.size[self.count] += 1
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)

    def mycid(self, v):
        self.validateVertex(v)
        return self.cid[v]

    def size(self, v):
        self.validateVertex(v)
        return self.size[self.cid[v]]

    def mycount(self):
        return self.count

    def connected(v, w):
        self.validateVertex(v)
        self.validateVertex(w)
        return self.mycid(v) == self.mycid(w)

    def validateVertex(self, v):
        V = len(self.marked)
        if v < 0 or v > v:
            raise Exception("vertex " + str(v) + " is not between 0 and " + str(V-1))

if __name__ == '__main__':
    myin = In(sys.argv[1])
    G = Graph(myin)
    cc = CC(G)

    m = cc.mycount()
    print(str(m) + " components")

    components = [None] * m
    for i in range(0, m):
        components[i] = queue.Queue()
    for v in range(0, G.Vertex()):
        components[cc.mycid(v)].put(v)

    for i in range(0, m):
        tmp = ""
        while not components[i].empty():
            tmp += (str(components[i].get()) + " ")
        print(tmp)
        print("\n")

