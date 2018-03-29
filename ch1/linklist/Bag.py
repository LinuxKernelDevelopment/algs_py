#!/home/hmsjwzb/python/bin/python3
from Node import Node

class Bag:
    def __init__(self):
        self.first = None
        self.current = None
        self.N = 0

    def add(self, item):
        oldfirst = self.first
        self.first.item = item
        self.first.next = oldfirst
        self.N += 1

    def size(self):
        return self.N

    def __iter__(self):
        self.current = self.first

    def __next__(self):
        if self.current.next == None:
            raise StopIteration
        return self.current.item


