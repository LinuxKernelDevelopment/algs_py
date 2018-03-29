#!/home/hmsjwzb/python/bin/python3

class QuickFindUF:
    def __init__(self, n):
        self.count = n
        self.id = [None] * n
        for i in range(n):
            self.id[i] = i

    def count_components(self):
        return self.count

    def find(self, p):
        self.validate(p)
        return self.id[p]

    def count(self):
        return self.count

    def validate(self, p):
        n = len(self.id)
        if p < 0 and p >= n:
            raise IndexError

    def connected(self, p, q):
        self.validate(p)
        self.validate(q)
        return self.id[p] == self.id[q]

    def union(self, p, q):
        self.validate(p)
        self.validate(q)
        pID = self.id[p]
        qID = self.id[q]

        if pID == qID: return

        for i in range(len(self.id)):
            if self.id[i] == pID:
                self.id[i] = qID

        self.count -= 1

