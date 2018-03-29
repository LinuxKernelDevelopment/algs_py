#!/home/hmsjwzb/python/bin/python3

import math
from StdIn import StdIn
from EdgeWeightedDigraph import EdgeWeightedDigraph
from BellmanFord import BellmanFordSP
from DirectedEdge import DirectedEdge

class Arbitrage:
    def __init__(self):
        pass


if __name__ == '__main__':
    myin = StdIn()
    V = myin.readInt()
    name = [None] * V

    G = EdgeWeightedDigraph(V, None, None)
    for v in range(0, V):
        name[v] = myin.readString()
        for w in range(0, V):
            rate = myin.readDouble()
            e = DirectedEdge(v, w, -math.log(rate))
            G.addEdge(e)

    spt = BellmanFordSP(G, 0)
    tmpstr = ""
    if spt.hasNegativeCycle():
        stake = 1000.0
        for e in spt.negativeCycle():
            tmpstr += (str(stake) + name[e.eto()])
            stake *= math.exp(-e.Weight())
            tmpstr += "= " + str(stake) + " " + name[e.efrom()] + "\n"
            print(tmpstr)
            tmpstr = ""
    else:
        print("No arbitrage opportunity")
