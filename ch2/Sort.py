#!/home/hmsjwzb/python/bin/python3

class Sort:
    def __init__(self):
        pass

    @staticmethod
    def sort(a):
        pass

    @staticmethod
    def less(v, w):
        return v < w

    @staticmethod
    def exch(a, i, j):
        a[i], a[j] = a[j], a[i]
        
    @staticmethod
    def show(a):
        for item in a:
            print(str(item) + " ", end = '')
        print('\n')

    @staticmethod
    def isSorted(a):
        for prev, curr in zip(li, li[1:]):
            if less(curr, prev): return False
        return True
