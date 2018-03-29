#!/home/hmsjwzb/python/bin/python3

from In import In
import sys
from Digraph import Digraph

class SymbolDigraph:
    def __init__(self, filename, delimiter):
        self.st = dict()
        self.keys = dict()
        delimiter = None
        myin = In(filename, delimiter)
        while myin.hasNextLine():
            a = myin.readLine().split(delimiter)
            for i in range(0, len(a)):
                if self.st.get(a[i]) == None:
                    self.st[a[i]] = len(self.st)

        for name in self.st.keys():
            self.keys[self.st[name]] = name

        self.graph = Digraph(len(self.st.keys()))
        myin = In(filename, '\n')
        while myin.hasNextLine():
            a = myin.readLine().split(' ')
            v = self.st.get(a[0])
            for i in range(1, len(a)):
                w = self.st.get(a[i])
                self.graph.addEdge(v, w)

    def contains(self, s):
        if self.st.get(s) == None:
            return False
        else:
            return True

    def index(self, s):
        return self.st.get(s)

    def indexOf(self, s):
        return self.get(s)

    def name(self, v):
        self.validateVertex(v)
        return self.keys[v]

    def nameOf(self, v):
        self.validateVertex(v)
        return self.keys[v]

    def G(self):
        return self.graph

    def digraph(self):
        return self.graph

    def validateVertex(self, v):
        Ver = self.graph.Vertex()
        if v < 0 or v >= Ver:
            raise("vertex %d is not between 0 and %d " % (v, Ver-1))

if __name__ == '__main__':
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    sg = SymbolDigraph(filename, delimiter)
    graph = sg.digraph()
    print(graph)
    while True:
        t = input()
        for v in graph.adj[sg.index(t)]:
            print("   %s" % sg.name(v))
