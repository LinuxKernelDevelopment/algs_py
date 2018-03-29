#!/home/hmsjwzb/python/bin/python3.5

class EdgeWeightedDirectedCycle:
    def __init__(self, G):
        self.marked = [None] * G.Vertex()
        self.onStack = [None] * G.Vertex()
        self.edgeTo = [None] * G.Vertex()
        self.cycle = []
        for v in range(0, G.Vertex()):
            if not self.marked[v]:
                self.dfs(G, v)


    def dfs(self, G, v):
        self.onStack[v] = True
        self.marked[v] = True
        for e in G.adj[v]:
            w = e.eto()

            if self.cycle != []:
                return
            elif not self.marked[w]:
                self.edgeTo[w] = e
                self.dfs(G, w)
            elif self.onStack[w]:
                self.cycle = []

                f = e
                while f.efrom() != w:
                    self.cycle += [f]
                    f = self.edgeTo[f.efrom()]
                self.cycle += [f]
                return
        self.onStack[v] = False

    def cycle(self):
        return self.cycle

    def hasCycle(self):
        return self.cycle != []

    def check(self):
        if self.hasCycle():
            first = None
            last = None
            for e in self.cycle():
                if first == None:
                    first = e
                if last != None:
                    if last.eto() != e.efrom():
                        print("cycle edges %s and %s not incident\n", last, e)
                        return False
                last = e

            if last.eto() != first.efrom():
                print("cycle edges %s and %s not incident\n", last, first)
                return False

        return True

if __name__ == '__main__':
    V = int(sys.argv[1])
    E = int(sys.argv[2])
    F = int(sys.argv[3])
    G = EdgeWeightedDigraph(V)
    vertices = [0] * V

