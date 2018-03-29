#!/home/hmsjwzb/python/bin/python3.5

import sys
from In import In
from Graph import Graph
from StdIn import StdIn

class SymbolGraph:
    def __init__(self, filename, delimiter):
        self.st = {}
        myin = In(filename, delimiter)
        while not myin.isEmpty():
            a = myin.readLine().split(delimiter)
            for element in a:
                if not self.st.get(element, None):
                    self.st[element] = len(self.st.keys())
        print("Done reading %s\n" % filename)
        
        self.keys = {}
        for name in self.st.keys():
            self.keys[self.st.get(name)] = name

        self.graph = Graph(len(self.st.keys()))
        myin = In(filename, delimiter)
        while myin.hasNextLine():
            a = myin.readLine().split(delimiter)
            v = self.st.get(a[0])
            for element in a[1:len(a)]:
                w = self.st.get(element)
                self.graph.addEdge(v, w)

    def contains(self, s):
        return self.st.get(s)

    def index(self, s):
        return self.st.get(s)

    def indexOf(self, s):
        return self.st.get(s)

    def name(self, v):
        self.validateVertex(v)
        return self.keys[v]

    def nameOf(self, v):
        self.validateVertex(v)
        return self.keys[v]

    def G(self):
        return self.graph

    def Graph(self):
        return self.graph

    def validateVertex(self, v):
        V = self.graph.Vertex()
        if v < 0 or v >= V:
            raise Exception("vertex %d is not between 0 and %d" % (v, V-1))

if __name__ == '__main__':
    print(sys.argv)
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    sg = SymbolGraph(filename, delimiter)
    graph = sg.Graph()
    mystdin = StdIn()
    while mystdin.hasNextLine():
        source = mystdin.readLine()
        print("source:%s" % source)
        if sg.contains(source):
            s = sg.index(source)
            print(graph.adj[s])
            for v in graph.adj[s]:
                print("    %s\n" % sg.name(v))
        else:
            print("input not contain \'%s\'\n" % sources)
