#!/home/hmsjwzb/python/bin/python3.5
from In import In
import sys
from Digraph import Digraph

class DirectedCycle:
    def __init__(self, G):
        self.marked = [False] * G.Vertex()
        self.onStack = [False] * G.Vertex()
        self.edgeTo = [0] * G.Vertex()
        self.cycle = []
        for v in range(0, G.Vertex()):
            if not self.marked[v] and self.cycle == []:
                self.dfs(G, v)

    def dfs(self, G, v):
        self.onStack[v] = True
        self.marked[v] = True
        for w in G.adj[v]:
            if self.cycle != []:
                return
            elif not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(G, w)
            elif self.onStack[w]:
                self.cycle = []
                x = v
                print(x, w)
                while x != w:
                    self.cycle += [x]
                    x = self.edgeTo[x]
                self.cycle += [w]
                self.cycle += [v]
        self.onStack[v] = False

    def hasCycle(self):
        return self.cycle != []

    def Cycle(self):
        return self.cycle

    def check(self):
        if self.hasCycle():
            first = -1
            last = -1
            for v in self.cycle():
                if first == -1:
                    first = v
                last = v
            if first != last:
                print("cycle begins with %d ends with %d\n" % (first, last))
                return False
        return True

if __name__ == '__main__':
    myin = In(sys.argv[1], None)
    G = Digraph(myin)

    finder = DirectedCycle(G)
    if finder.hasCycle():
        print("Directed cycle: ")
        tmpstr = ""
        for v in finder.Cycle():
            tmpstr += (str(v) + " ")
        print(tmpstr)
        print("\n")
    else:
        print("No directed cycle")
    print("\n")
