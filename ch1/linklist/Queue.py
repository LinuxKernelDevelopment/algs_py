#!/home/hmsjwzb/python/bin/python3

from Node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.N = 0

    def isEmpty(self):
        return self.first == None

    def size(self):
        return self.N

    def enqueue(self, item):
        oldlast = self.last
        self.last = Node()
        self.last.item = item
        self.last.next = None
        if self.isEmpty(): self.first = self.last
        else:   oldlast.next = self.last
        self.N += 1

    def dequeue(self):
        item = self.first.item
        self.first = self.first.next
        if self.isEmpty(): self.last = None
        self.N -= 1
        return item
