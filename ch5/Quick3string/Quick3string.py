#!/home/hmsjwzb/python/bin/python3
import sys
sys.path.append("/home/hmsjwzb/intel/Algorithm/tools/")
from StdIn import StdIn

CUTOFF = 15
class Quick3string:
    def __init__(self):
        pass

    def sort(self, a):
        self.sort_r(a, 0, len(a)-1, 0)

    def charAt(self, s, d):
        if d == len(s):
            return -1
        return s[d]

    def sort_r(self, a, lo, hi, d):
        if hi <= lo + CUTOFF:
            self.insertion(a, lo, hi, d)
            return
        lt = lo
        gt = hi
        v = self.charAt(a[lo], d)
        i = lo + 1
        while i <= gt:
            t = self.charAt(a[i], d)
            if t < v:
                self.exch(a, lt, i)
                lt += 1
                i += 1
            elif t > v:
                self.exch(a, i, gt)
                gt -= 1
            else:
                i += 1

        self.sort_r(a, lo, lt-1, d)
        if ord(v) >= 0:
            self.sort_r(a, lt, gt, d+1)
        self.sort_r(a, gt+1, hi, d)

    def insertion(self, a, lo, hi, d):
        for i in range(lo, hi+1):
            for j in range(i, lo, -1):
                if self.less(a[j], a[j-1], d):
                    self.exch(a, j, j-1)

    def exch(self, a, i, j):
        a[i], a[j] = a[j], a[i]

    def less(self, v, w, d):
        for i in range(d, min(len(v), len(w))):
            if self.charAt(v, i) < self.charAt(w, i):
                return True
            if self.charAt(v, i) > self.charAt(w, i):
                return False
        return len(v) < len(w)

    def isSorted(self, a):
        for i in range(1, len(a)):
            if not self.less(a[i-1], a[i]):
                return False
        return True


if __name__ == '__main__':
    myin = StdIn()
    a = myin.readAllStrings()
    n = len(a)

    q3 = Quick3string()
    q3.sort(a)

    for i in range(0, n):
        print(a[i])
