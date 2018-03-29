#!/home/hmsjwzb/python/bin/python3.5

import math

class Edge:
    def __init__(self, v, w, weight):
        if v < 0:
            raise Exception("vertex index must be a nonnegative integer")
        if w < 0:
            raise Exception("vertex index must be a nonnegative integer")
        if math.isnan(weight):
            raise ValueError("Weight is NaN")
        self.v = v
        self.w = w
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def weight(self):
        return self.weight

    def either(self):
        return self.v

    def other(self, vertex):
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        else:
            raise ValueError("Illegal endpoint")

    def compareTo(self, that):
        return self.weight > that.weight

    def __str__(self):
        s = "%d-%d %.5f" % (self.v, self.w, self.weight)
        return s

if __name__ == '__main__':
    e = Edge(12, 34, 5.67)
    print(e)

