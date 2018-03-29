#!/home/hmsjwzb/python/bin/python3
from StdIn import StdIn

class Node:
    left = None
    right = None
    def __init__(self, key, val, size):
        self.key = key
        self.val = val
        self.size = size

class BST:
    root = None

    def __init__(self):
        pass

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.size_r(self.root)

    def size_r(self, x):
        if x == None: return 0
        else: return x.size

    def height(self):
        return self.height_r(self.root)

    def height_r(self, x):
        if x == None: return 0
        left_hight = 1 + self.height_r(x.left)
        right_hight = 1 + self.height_r(x.right)
        if left_hight > right_hight:
            return left_hight
        else:
            return right_hight

    def contains(self, key):
        return self.get(key) != None

    def get(self, key):
        return self.get_r(self.root, key)

    def get_r(self, x, key):
        cmp = ord(key) - ord(x.key)
        if cmp < 0:
            return self.get_r(x.left, key)
        elif cmp > 0:
            return self.get_r(x.right, key)
        else:
            return x.val

    def put(self, key, val):
        if val == None:
            self.delete(key)
            return None
        self.root = self.put_r(self.root, key, val)

    def put_r(self, x, key, val):
        if x == None:
            return Node(key, val, 1)
        cmp = ord(key) - ord(x.key)
        if cmp < 0:
            x.left = self.put_r(x.left, key, val)
        elif cmp > 0:
            x.right = self.put_r(x.right, key, val)
        else:
            x.val = val
        x.size = 1 + self.size_r(x.left) + self.size_r(x.right)
        return x

    def deleteMin(self):
        self.root = self.deleteMin_r(self.root)

    def deleteMin_r(self, x):
        if x.left == None:
            return x.right
        x.left = self.deleteMin_r(x.left)
        x.size = self.size(x.left) + self.size(x.right) + 1
        return x

    def deleteMax(self):
        self.root = self.deleteMax_r(self.root)

    def deleteMax(self, x):
        if x.right == None:
            return x.left
        x.right = self.deleteMax_r(x.right)
        x.size = size(x.left) + size(x.right) + 1
        return x

    def delete(self, key):
        self.root = self.delete_r(self.root, key)

    def delete_r(self, x, key):
        if x == None:
            return None

        cmp = key - x.key
        if cmp < 0:
            x.left = self.delete_r(x.left, key)
        elif cmp > 0:
            x.right = self.delete_r(x.right, key)
        else:
            if x.right == None:
                return x.left
            if x.left == None:
                return x.right
            t = x
            x = self.min(t.right)
            x.right = self.deleteMin(t.right)
            x.left = t.left
        x.size = self.size(x.left) + self.size(x.right) + 1
        return x

    def min(self):
        return self.min_r(self.root).key

    def min_r(self, x):
        if x.left == None: return x
        else:              return self.min_r(x.left)

    def max(self):
        return self.max_r(self.root).key

    def max_r(self, x):
        if x.right == None: return x
        else:              return self.max_r(x.right)

    def floor(self, key):
        x = self.floor_r(self.root, key)
        if x == None:
            return None
        else:
            return x.key

    def floor_r(x, key):
        if x == None:
            return None
        cmp = ord(key) - ord(x.key)
        if cmp == 0:
            return x
        if cmp < 0:
            return self.floor_r(x.left, key)
        t = self.floor_r(x.right, key)
        if t != None:
            return t
        else:
            return x


    def select(self, k):
        x = self.select_r(self.root, k)
        return x.key

    def select_r(self, x, k):
        t = self.size_r(x.left)
        if t > k:
            return self.select_r(x.left, k)
        elif t < k:
            return self.select_r(x.right, k-t-1)
        else:
            return x

    def rank(self, key):
        return self.rank_r(key, self.root)

    def rank_r(self, key, x):
        if x == None: return 0
        if key < x.key:
            return self.rank_r(key, x.left)
        elif key > x.key:
            return 1 + self.size_r(x.left) + self.rank_r(key, x.right)
        else:
            return self.size_r(x.left)

    def keys(self):
        q = []
        self.keys_r(self.root, q, self.min(), self.max())
        return q

    def keys_r(self, x, q, lo, hi):
        if x == None: return
        cmplo = ord(lo) - ord(x.key)
        cmphi = ord(hi) - ord(x.key)
        if cmplo < 0:
            self.keys_r(x.left, q, lo, hi)
        if cmplo <= 0 and cmphi >= 0:
            q.append(x.key)
        if cmphi > 0:
            self.keys_r(x.right, q, lo, hi)
        

if __name__ == '__main__':
    st = BST()
    i = 0
    StdIn = StdIn()
    while not StdIn.isEmpty():
        key = StdIn.readString()
        i += 1
        st.put(key, i)

    ##print(st.select(3))
    print(st.rank('L'))
    print(st.height())

    for s in st.keys():
        print(s + " " + str(st.get(s)))
