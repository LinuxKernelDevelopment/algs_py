#!/home/hmsjwzb/python/bin/python3.5

from StdIn import StdIn

class QuickUnionUF:
    def __init__(self, n):
        self.parent = [None] * n
        self.count = n
        for i in range(0, n):
            self.parent[i] = i

    def Count(self):
        return self.count

    def find(self, p):
        self.validate(p)
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def validate(self, p):
        n = len(self.parent)
        if p < 0 or p > n:
            raise ValueError("index %d is not between 0 and %d" % (p, n-1))

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        self.parent[rootP] = rootQ
        self.count -= 1


if __name__ == '__main__':
    myin = StdIn()
    n = myin.readInt()
    uf = QuickUnionUF(n)
    while myin.isEmpty():
        p = myin.readInt()
        q = myin.readInt()
        if uf.connected(p, q):
            continue
        uf.union(p, q)
        print(str(p) + " " + str(q))
    print(str(uf.Count()) + " components")
