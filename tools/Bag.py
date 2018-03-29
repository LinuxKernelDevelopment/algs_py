#!/home/hmsjwzb/python/bin/python3
from Node import Node

class Bag:
    def __init__(self):
        self.first = None
        self.current = None
        self.N = 0

    def add(self, item):
        oldfirst = self.first
        first = Node()
        first.item = item
        first.next = oldfirst
        self.first = first
        self.N += 1

    def size(self):
        return self.N

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        if self.current == None:
            raise StopIteration
        item = self.current.item
        self.current = self.current.next
        return item


