#!/home/hmsjwzb/python/bin/python3
import sys
sys.path.append("/home/hmsjwzb/intel/Algorithm/tools/")
from StdIn import StdIn

BITS_PER_BYTE = 8
BITS_PER_INT  = 32
R             = 256
CUTOFF        = 15

class MSD:
    def __init__(self):
        pass

    def sort(self, a):
        n = len(a)
        aux = [None] * n
        self.sort_r(a, 0, n-1, 0, aux)

    def charAt(self, s, d):
        if d == len(s):
            return -1
        return s[d]

    def sort_r(self, a, lo, hi, d, aux):
        if hi <= lo + CUTOFF:
            self.insertion(a, lo, hi, d)
            return

        count = [0] * (R + 2)
        for i in range(lo, hi+1):
            c = self.charAt(a[i], d)
            count[ord(c)+2] += 1

        for r in range(0, R+1):
            count[r+1] += count[r]

        for i in range(lo, hi+1):
            c = self.charAt(a[i], d)
            aux[count[ord(c)+1]] = a[i]
            count[ord(c)+1] += 1

        for i in range(lo, hi):
            a[i] = aux[i-lo]

        for r in range(0, R):
            self.sort_r(a, lo + count[r], lo + count[r+1] - 1, d+1, aux)


    def insertion(self, a, lo, hi, d):
        for i in range(lo, hi+1):
            for j in range(i, lo, -1):
                if self.less(a[j], a[j-1], d):
                    self.exch(a, j, j-1)

    def exch(self, a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def less(self, v, w, d):
        for i in range(d, min(len(v), len(w))):
            if self.charAt(v, i) < self.charAt(w, i):
                return True
            if self.charAt(v, i) > self.charAt(w, i):
                return False
        return len(v) < len(w)

if __name__ == '__main__':
    myin = StdIn()
    a = myin.readAllStrings()
    n = len(a)
    msd = MSD()
    msd.sort(a)
    for i in range(0, n):
        print(a[i])
