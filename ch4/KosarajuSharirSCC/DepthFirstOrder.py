#!/home/hmsjwzb/python/bin/python3

import queue
from In import In
import sys
from Digraph import Digraph

class DepthFirstOrder:
    def __init__(self, G):
        if type(G) is Digraph:
            self.Digraph_init(G)
        else:
            self.EdgeWeightedDigraph_init(G)

    def EdgeWeightedDigraph_init(self, G):
        pass

    def Digraph_init(self, G):
        self.pre  = [0] * G.Vertex()
        self.post = [0] * G.Vertex()
        self.postorder = []
        self.preorder = []
        self.marked = [False] * G.Vertex()
        self.preCounter = 0
        self.postCounter = 0
        for v in range(0, G.Vertex()):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G, v):
        if type(G) is Digraph:
            self.dfs_di(G, v)
        else:
            pass

    def dfs_di(self, G, v):
        self.marked[v] = True
        self.preCounter += 1
        self.pre[v] = self.preCounter
        self.preorder.append(v)
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs_di(G, w)
        self.postorder.append(v)
        self.postCounter += 1
        self.post[v] = self.postCounter

    def get_pre(self, v):
        self.validateVertex(v)
        return self.pre[v]

    def get_post(self, v):
        self.validateVertex(v)
        return self.post[v]

    def postorder_queue(self):
        return self.postorder

    def preorder_queue(self):
        return self.preorder

    def reversePost(self):
        reverse = []
        for v in self.postorder:
            reverse = [v] + reverse
        return reverse

    def check(self):
        r = 0
        for v in self.postorder_queue():
            if self.get_post(v) != r:
                print("pre(v) and pre() inconsistent")
                return False
            r += 1
        return True

    def validateVertex(self, v):
        V = len(self.marked)
        if v < 0 or v >= V:
            raise("vertex %d is not between 0 and %d" % (v, V-1))

if __name__ == '__main__':
    myin = In(sys.argv[1], None)
    G = Digraph(myin)

    dfs = DepthFirstOrder(G)
    print("v    pre    post")
    for v in range(0, G.Vertex()):
        print("%4d %4d %4d"% (v, dfs.get_pre(v), dfs.get_post(v)))

    print("Preorder: \n")
    s = ""
    for v in dfs.preorder_queue():
        s += "%s " % v
    s += '\n'
    print(s)

    print("Postorder: \n")
    s = ""
    for v in dfs.postorder_queue():
        s += "%s " % v
    s += '\n'
    print(s)

    print("Reverse postorder: ")
    s = ""
    for v in dfs.reversePost():
        s += "%s " % v
    s += '\n'
    print(s)
