#!/home/hmsjwzb/python/bin/python3

from StdIn import StdIn

RED = True
BLACK = False

class Node:
    left = None
    right = None
    def __init__(self, key, val, color, size):
        self.key = key
        self.val = val
        self.color = color
        self.size = size

class RedBlackBST:
    def __init__(self):
        self.root = None

    def isRed(self, x):
        if x == None:
            return False
        return x.color == RED

    def size_n(self, x):
        if x == None:
            return 0
        else:
            return x.size

    def size(self):
        return self.size_n(self.root)

    def isEmpty(self):
        return self.root == None

    def get(self, key):
        if key == None:
            raise Exception('argument to get() is null')
        return self.get_n(self.root, key)

    def get_n(self, x, key):
        while x != None:
            cmp = key.compareTo(x.key)
            if cmp < 0: x = x.left
            elif cmp > 0: x = x.right
            else:           return x.val
        return None

    def contains(self, key):
        return self.get(key) != None

    def put(self, key, val):
        if key == None:
            raise Exception('first argument to put() is null')
        if val == None:
            self.delete(key)
            return

        self.root = self.put_n(self.root, key, val)
        self.root.color = BLACK

    def put_n(self, h, key, val):
        if h == None:
            return Node(key, val, RED, 1)
        
        cmp = key.compareTo(h.key)
        if cmp < 0:
            h.left = self.put_n(h.left, key, val)
        elif cmp > 0:
            h.right = self.put_n(h.right, key, val)
        else:
            h.val = val

        if self.isRed(h.right) and not self.isRed(h.left):
            h = self.rotateLeft(h)
        if self.isRed(h.left) and self.isRed(h.left.left):
            h = self.rotateRight(h)
        if self.isRed(h.left) and self.isRed(h.right):
            self.flipColors(h)
        h.size = self.size_n(h.left) + self.size_n(h.right) + 1

        return h

    def deleteMin(self):
        if self.isEmpty():
            raise Exception("BST underflow")

        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = RED
        self.root = self.deleteMin_r(self.root)
        if not self.isEmpty():
            self.root.color = BLACK

    def deleteMin_r(self, h):
        if h.left == None:
            return None

        if not self.isRed(h.left) and not self.isRed(h.left.left):
            h = self.MoveRedLeft(h)

        h.left = self.deleteMin(h.left)
        return self.balance(h)

    def deleteMax(self):
        if self.isEmpty():
            raise Exception("BST underflow")

        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            root.color = RED

        root = deleteMax_r(self.root)
        if not self.isEmpty():
            self.root.color = BLACK

    def deleteMax_r(self, h):
        if self.isRed(h.left):
            h = self.rotateRight(h)

        if h.right == None:
            return None

        if not self.isRed(h.right) and not self.isRed(h.right.left):
            h = self.moveRedRight(h)

        h.right = deleteMax_r(h.right)

        return self.balance(h)

    def delete(self, key):
        if key == None:
            raise Exception("argument to delete() is null")
        if not self.contains(key):
            return

        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = RED

        self.root = self.delete_r(self.root, key)
        if not self.isEmpty():
            self.root.color = BLACK

    def delete_r(self, h, key):
        if key.compareTo(h.key) < 0:
            if not self.isRed(h.left) and not self.isRed(h.left.left):
                h = self.MoveRedLeft(h)
            h.left = self.delete_r(h.left, key)
        else:
            if self.isRed(h.left):
                h = self.rotateRight(h)
            if key.compareTo(h.key) == 0 and h.right == None:
                return None
            if not self.isRed(h.right) and not self.isRed(h.right.left):
                h = moveRedRight(h)
            if key.compareTo(h.key) == 0:
                x = self.min(h.right)
                h.key = x.key
                h.val = x.val

                h.right = self.deleteMin(h.right)
            else:
                h.right = self.delete(h.right, key)
        return self.balance(h)

    def rotateRight(self, h):
        #print("%s rotate right" % h.key)
        x = h.left
        h.left = x.right
        x.right = h
        x.color = x.right.color
        x.right.color = RED
        x.size = h.size
        h.size = self.size_n(h.left) + self.size_n(h.right) + 1
        return x

    def rotateLeft(self, h):
        #print("%s rotate left" % h.key)
        x = h.right
        h.right = x.left
        x.left = h
        x.color = x.left.color
        x.left.color = RED
        x.size = h.size
        h.size = self.size_n(h.left) + self.size_n(h.right) + 1
        return x

    def flipColors(self, h):
        #print("%s flip color" % h.key)
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    def MoveRedLeft(self, h):
        self.flipColors(h)
        if self.isRed(h.right.left):
            h.right = self.rotateRight(h.right)
            h = self.rotateLeft(h)
            self.flipColors(h)
        return h

    def MoveRedRight(self, h):
        flipColor(h)
        if isRed(h.left.left):
            h = rotateRight(h)
            flipColors(h)
        return h

    def balance(self, h):
        if self.isRed(h.right):
            h = self.rotateLeft(h)
        if self.isRed(h.left) and self.isRed(h.left.left):
            h = self.rotateRight(h)
        if self.isRed(h.left) and self.isRed(h.right):
            self.flipColors(h)

        h.size = self.size_n(h.left) + self.size_n(h.right) + 1
        return h

    def min(self):
        return self.min_r(self.root).key

    def min_r(self, x):
        if x.left == None:
            return x
        else:
            return self.min_r(x.left)

    def max(self):
        return self.max_r(self.root).key

    def max_r(self, x):
        if x.right == None:
            return x
        else:
            return self.max_r(x.right)

    def floor(self, key):
        if key == None:
            raise Exception("argument to floor() is null")
        if self.isEmpty():
            raise Exception("called floor() with empty symbol table")
        x = self.floor(self.root, key)
        if x == None:
            return None
        else:
            return x.key

    def floor_r(self, x, key):
        if x == None:
            return None
        cmp = key.compareTo(x.key)
        if cmp == 0:
            return x
        if cmp < 0:
            return self.floor_r(x.left, key)
        t = self.floor_r(x.right, key)
        if t != None:
            return t
        else:
            return x

    def ceiling(self, key):
        if key == None:
            raise Exception("argument to ceiling() is null")
        if self.isEmpty():
            raise Exception("called ceiling() with empty symbol table")
        x = self.ceiling_r(root, key)
        if x == None:
            return None
        else:
            return x.key
        
    def ceiling_r(self, x, key):
        if x == None:
            return None
        cmp = key.compareTo(x.key)
        if cmp == 0:
            return x
        if cmp > 0:
            return self.ceiling_r(x.right, key)
        t = self.ceiling_r(x.left, key)
        if t != None:
            return t
        else:
            return x

    def select(self, k):
        if k < 0 or k >= self.size():
            raise Exception("called select() with invalid argument: " + k)
        x = select_r(self.root, k)
        return x.key

    def select(self, x, k):
        t = self.size_n(x.left)
        if t > k:
            return self.select(x.left, k)
        elif t < k:
            return self.select(x.right, k-t-1)
        else:
            return x

    def rank(self, key):
        if key == None:
            raise Exception("argument to rank() is null")
        return self.rank_r(key, self.root)

    def rank_r(self, x):
        if x == None:
            return 0
        cmp = key.compareTo(x.key)
        if cmp < 0:
            return self.rank_r(key, x.left)
        elif cmp > 0:
            return 1 + self.size_n(x.left) + self.rank_r(key, x.right)
        else:
            return self.size_n(x.left)

    def Keys(self):
        return self.keys(self.min(), self.max())
        

    def keys(self, lo, hi):
        q = []
        self.keys_r(self.root, q, lo, hi)
        return q

    def keys_r(self, x, q, lo, hi):
        if x == None:
            return
        cmplo = lo.compareTo(x.key)
        cmphi = hi.compareTo(x.key)
        if cmplo < 0:
            self.keys_r(x.left, q, lo, hi)
        if cmplo <= 0 and cmphi >= 0:
            q.append(x.key)
        if cmphi > 0:
            self.keys_r(x.right, q, lo, hi)

    def size_rank(self, lo, hi):
        if lo == None:
            raise Exception("first argument to size() is null")
        if hi == None:
            raise Exception("second argument to size() is null")

        if lo.compareTo(hi) > 0:
            return 0
        if self.contains(hi):
            return self.rank(hi) - self.rank(lo) + 1
        else:
            return self.rank(hi) - self.rank(lo)

    def check(self):
        if not self.isBST():
            print("Not in symmetric order")
        if not self.isSizeConsistent():
            print("Subtree counts not consistent")
        if not self.isRankConsistent():
            print("Ranks not consistent")
        if not self.is23():
            print("Not a 2-3 tree")
        if not self.isBalanced():
            print("Not balanced")
        return self.isBST() and self.isSizeConsistent() and self.isRankConsistent() and self.is23() and self.isBalanced()

    def isBST(self):
        return self.isBST_r(self.root, None, None)

    def isBST_r(self, x, min, max):
        if x == None:
            return True
        if min != None and x.key.compareTo(min) <= 0:
            return False
        if max != None and x.key.compareTo(max) >= 0:
            return False
        return self.isBST_r(x.left, min, x.key) and self.isBST_r(x.right, x.key, max)

    def isSizeConsistent(self):
        return self.isSizeConsistent_r(self.root)

    def isSizeConsistent_r(self, x):
        if x == None:
            return True
        if x.size != self.size(x.left) + self.size(x.right) + 1:
            return False
        return self.isSizeConsistent_r(x.left) and self.isSizeConsistent_r(x.right)


    def isRankConsistent(self):
        for i in range(0, self.size()):
            if i != self.rank(select(i)):
                return False
        for key in self.keys():
            if key.compareTo(self.select(self.rank(key))) != 0:
                return False
        return True

    def is23(self):
        return self.is23_r(self.root)

    def is23_r(self, x):
        if x == None:
            return True
        if self.isRed(x.right):
            return False
        if x != self.root and self.isRed(x) and self.isRed(x.left):
            return False
        return self.is23_r(x.left) and self.is23_r(x.right)

    def isBalanced(self):
        black = 0
        x = self.root
        while x != None:
            if not self.isRed(x):
                black += 1
            x = x.left
        return self.isBalanced_r(self.root, black)

    def isBalanced_r(self, x, black):
        if x == None:
            return black == 0
        if not self.isRed(x):
            black -= 1
        return self.isBalanced_r(x.left, black) and self.isBalanced(x.right, black)
