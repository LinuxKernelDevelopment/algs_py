#!/home/hmsjwzb/python/bin/python3
from StdIn import StdIn

from Sort import Sort
class Quick3way(Sort):
    @staticmethod
    def __sort(a, lo, hi):
        if hi <= lo:
            return
        lt = lo; i = lo + 1; gt = hi
        v = a[lo]
        while i <= gt:
            if a[i] < v:
                Quick3way.exch(a, lt, i)
                lt += 1; i += 1
            elif a[i] > v:
                Quick3way.exch(a, i, gt)
                gt -= 1
            else:
                i += 1
        Quick3way.__sort(a, lo, lt - 1)
        Quick3way.__sort(a, gt + 1, hi)

    @staticmethod
    def sort(a):
        Quick3way.__sort(a, 0, len(a)-1)
        
        

if __name__ == '__main__':
    #a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    StdIn = StdIn()
    a = StdIn.readAllStrings()
    Quick3way.sort(a)
    Quick3way.show(a)
