#!/home/hmsjwzb/python/bin/python3.6
import sys
from Digraph import Digraph
from DirectedDFS import DirectedDFS

class NFA:
    regexp = None
    m = 0
    def __init__(self, regexp):
        self.regexp = regexp
        self.m = len(regexp)
        self.graph = Digraph(self.m+1)
        ops = []
        for i in range(0, self.m):
            lp = i
            if regexp[i] == '(' or regexp[i] == '|':
                ops += [i]
            elif regexp[i] == ')':
                or_ = ops.pop()
                if regexp[or_] == '|':
                    lp = ops.pop()
                    self.graph.addEdge(lp, or_+1)
                    self.graph.addEdge(or_, i)
                elif regexp[or_] == '(':
                    lp = or_
                else:
                    assert False
            if i < self.m -1 and regexp[i+1] == '*':
                self.graph.addEdge(lp, i+1)
                self.graph.addEdge(i+1, lp)
            if regexp[i] == '(' or regexp[i] == '*' or regexp[i] == ')':
                self.graph.addEdge(i, i+1)
        if len(ops) != 0:
            raise ValueError("Invalid regular expression")

    def recognizes(self, txt):
        dfs = DirectedDFS(self.graph, [0])
        pc = []
        for v in range(0, self.graph.Vertex()):
            if dfs.marked[v]:
                pc += [v]
        for i in range(0, len(txt)):
            if txt[i] == '*' or txt[i] == '|' or txt[i] == '(' or txt[i] == ')':
                raise ValueError("text contains the metacharacter %s" % (txt[i]))

            match = []
            for v in pc:
                if v == self.m:
                    continue
                if self.regexp[v] == txt[i] or self.regexp[v] == '.':
                    match += [v+1]
            dfs = DirectedDFS(self.graph, match)
            pc = []
            for v in range(0, self.graph.Vertex()):
                if dfs.marked[v]:
                    pc += [v]
            if len(pc) == 0:
                return False
        for v in pc:
            if v == self.m:
                return True
        return False

if __name__ == '__main__':
    regexp = "(" + sys.argv[1] + ")"
    txt = sys.argv[2]
    nfa = NFA(regexp)
    print(nfa.recognizes(txt))
