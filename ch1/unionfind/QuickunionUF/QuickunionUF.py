#!/home/hmsjwzb/python/bin/python3

class QuickUnionUF:
    def __init__(self, n):
        self.count = n
        self.parent = [None] * n
        for i in range(n):
            self.parent[i] = i

    def count_components(self):
        return self.count

    def find(self, p):
        self.validate(p)
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def count(self):
        return self.count

    def validate(self, p):
        n = len(self.parent)
        if p < 0 and p >= n:
            raise IndexError

    def connected(self, p, q):
        self.validate(p)
        self.validate(q)
        return self.parent[p] == self.parent[q]

    def union(self, p, q):
        self.validate(p)
        self.validate(q)
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        self.parent[rootP] = rootQ
        self.count -= 1
