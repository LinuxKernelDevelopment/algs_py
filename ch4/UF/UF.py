#!/home/hmsjwzb/python/bin/python3.5

from StdIn import StdIn

class UF:
    def __init__(self, n):
        if n < 0:
            raise Exception()
        self.count = n
        self.parent = [None] * n
        self.rank = [None] * n
        for i in range(0, n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, p):
        self.validate(p)
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def Count(self):
        return self.count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return

        if self.rank[rootP] < self.rank[rootQ]: self.parent[rootP]= rootQ
        elif self.rank[rootP] > self.rank[rootQ]: self.parent[rootQ] = rootP
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1
        self.count -= 1

    def validate(self, p):
        n = len(self.parent)
        if p < 0 or p >= n:
            raise OverflowError('index %d is not between 0 and %d' % (p, n-1))

if __name__ == '__main__':
   myin = StdIn()
   n = myin.readInt()
   uf = UF(n)
   while not myin.isEmpty():
       p = myin.readInt()
       q = myin.readInt()
       if uf.connected(p, q): continue
       uf.union(p, q)
       print("%d %d" % (p, q))
    print('a')
    print(str(uf.Count()) + " components\n")
