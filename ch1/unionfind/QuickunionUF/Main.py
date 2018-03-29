#!/home/hmsjwzb/python/bin/python3

from QuickunionUF import QuickUnionUF
from StdIn import StdIn

if __name__ == '__main__':
    MyStdIn = StdIn()
    n = MyStdIn.readInt()

    uf = QuickUnionUF(n)
    while not MyStdIn.isEmpty():
        p = MyStdIn.readInt()
        q = MyStdIn.readInt()
        if uf.connected(p, q): continue
        uf.union(p, q)
        print(str(p) + " " + str(q))

    print(str(uf.count_components()) + " components")
    
