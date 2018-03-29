#!/home/hmsjwzb/python/bin/python3

from Sort import Sort
from StdIn import StdIn

class MergeBU(Sort):
    @staticmethod
    def sort(a):
        N = len(a)
        MergeBU.aux = [None] * N
        sz = 1
        while sz < N:
            for lo in range(0, N - sz, 2 * sz):
                MergeBU.merge(a, lo, lo+sz-1, min(lo+sz+sz-1, N-1))
            sz = sz + sz

    '''@staticmethod
    def mergesort(a, lo, hi):
        if hi <= lo:
            return
        mid = lo + (hi - lo) // 2
        Merge.mergesort(a, lo, mid)
        Merge.mergesort(a, mid+1, hi)
        Merge.merge(a, lo, mid, hi)'''

    @staticmethod
    def merge(a, lo, mid, hi):
        i = lo
        j = mid + 1
        for k in range(lo, hi + 1):
            MergeBU.aux[k] = a[k]
        
        for k in range(lo, hi + 1):
            #print(str(i) + ' ' + str(Merge.aux[i]) + ' ' + str(j) + ' ' + str(Merge.aux[j]))
            if i > mid:
                a[k] = MergeBU.aux[j]
                j += 1
            elif j > hi: 
                a[k] = MergeBU.aux[i]
                i += 1
            elif MergeBU.less(MergeBU.aux[j],  MergeBU.aux[i]): 
                a[k] = MergeBU.aux[j]
                j += 1
            else:
                a[k] = MergeBU.aux[i]
                i += 1
            

if __name__ == '__main__':
    StdIn = StdIn()
    a = StdIn.readAllStrings()
    MergeBU.sort(a)
    MergeBU.show(a)
