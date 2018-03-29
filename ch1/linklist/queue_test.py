#!/home/hmsjwzb/python/bin/python3
import sys
from Queue import Queue
from StdIn import StdIn
if __name__ == '__main__':
    q = Queue()
    In = StdIn()
    while not In.isEmpty():
        item = In.readString()
        if item != '-':
            q.enqueue(item)
        elif not q.isEmpty():
            print(q.dequeue() + " ")
    print("(" + str(q.size()) + " left on queue)")
