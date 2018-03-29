#!/home/hmsjwzb/python/bin/python3
from StdIn import StdIn

from Sort import Sort
class Quick(Sort):
    @staticmethod
    def Sort(a):
        Quick.sort(a, 0, len(a)-1)
    
    @staticmethod
    def sort(a, lo, hi):
        if hi <= lo: return
        j = Quick.partition(a, lo, hi)
        Quick.sort(a, lo, j-1)
        Quick.sort(a, j+1, hi)

    @staticmethod
    def partition(a, lo, hi):
        i = lo
        j = hi+1
        v = a[lo]
        while True:
            i += 1
            while Quick.less(a[i], v): 
                if i == hi:
                    break
                i += 1

            j -= 1
            while Quick.less(v, a[j]):
                if j == lo:
                    break
                j -= 1

            if i >= j:
                break
            Quick.exch(a, i, j)
        Quick.exch(a, lo, j)
        return j

if __name__ == '__main__':
    #a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    StdIn = StdIn()
    a = StdIn.readAllStrings()
    Quick.Sort(a)
    Quick.show(a)
