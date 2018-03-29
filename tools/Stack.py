#!/home/hmsjwzb/python/bin/python3

from Node import Node

class Stack:
    def __init__(self):
        self.first = None
        self.N = 0

    def isEmpty(self):
        return self.first == None

    def size(self):
        return self.N

    def push(self, item):
        oldfirst = self.first
        self.first = Node()
        self.first.item = item
        self.first.next = oldfirst
        self.N += 1

    def pop(self):
        item = self.first.item
        first = self.first.next
        self.N -= 1
        return item

