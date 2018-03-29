#!/home/hmsjwzb/python/bin/python3

from MyNode import Node
from StdIn import StdIn

class SequentialSearchST:
    def __init__(self):
        self.n = 0
        self.first = None

    def contains(self, key):
        return self.get(key) != None


    def get(self, key):
        x = self.first
        while x != None:
            if key == x.key:
                return x.val
            x = x.next
        return None

    def put(self, key, val):
        x = self.first
        while x != None:
            if key == x.key:
                x.val = val
                return
            x = x.next
        self.first = Node(key, val, self.first)
        self.n += 1

    def delete(key):
        self.first = delete_r(self.first, key)

    def delete_r(x, key):
        if x == None:
            return None
        if key == x.key:
            self.n -= 1
            return x.next
        x.next = delete(x.next, key)
        return x

    def keys(self):
        x = self.first
        while x != None:
            yield x.key
            x = x.next

if __name__ == '__main__':
    st = SequentialSearchST()
    In = StdIn()
    i = 0
    while not In.isEmpty():
        key = In.readString()
        st.put(key, i)
        i += 1
    for s in st.keys():
        print(s + " " + str(st.get(s)))
