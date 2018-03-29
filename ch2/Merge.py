#!/home/hmsjwzb/python/bin/python3

from Sort import Sort
from StdIn import StdIn

class Merge(Sort):
    @staticmethod
    def sort(a):
        Merge.aux = [None] * (len(a))
        Merge.mergesort(a, 0, len(a) - 1)

    @staticmethod
    def mergesort(a, lo, hi):
        if hi <= lo:
            return
        mid = lo + (hi - lo) // 2
        Merge.mergesort(a, lo, mid)
        Merge.mergesort(a, mid+1, hi)
        Merge.merge(a, lo, mid, hi)

    @staticmethod
    def merge(a, lo, mid, hi):
        i = lo
        j = mid + 1
        for k in range(lo, hi + 1):
            Merge.aux[k] = a[k]
        
        for k in range(lo, hi + 1):
            #print(str(i) + ' ' + str(Merge.aux[i]) + ' ' + str(j) + ' ' + str(Merge.aux[j]))
            if i > mid:
                a[k] = Merge.aux[j]
                j += 1
            elif j > hi: 
                a[k] = Merge.aux[i]
                i += 1
            elif Merge.less(Merge.aux[j],  Merge.aux[i]): 
                a[k] = Merge.aux[j]
                j += 1
            else:
                a[k] = Merge.aux[i]
                i += 1
            

if __name__ == '__main__':
    StdIn = StdIn()
    a = StdIn.readAllStrings()
    Merge.sort(a)
    Merge.show(a)
