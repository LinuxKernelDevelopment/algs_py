#!/home/hmsjwzb/python/bin/python3

class DirectedEdge:
    def __init__(self, v, w, weight):
        if v < 0:
            raise ValueError("Vertex names must be nonnegative integers")
        if w < 0:
            raise ValueError("Vertex names must be nonnegative integers")
        self.v = v
        self.w = w
        self.weight = weight

    def efrom(self):
        return self.v

    def eto(self):
        return self.w

    def toString(self):
        return "%d -> %d, %f" % (self.v, self.w, self.weight)

    def __str__(self):
        return self.toString()

if __name__ == '__main__':
    e = DirectedEdge(12, 34, 5.67)
    print(e)
