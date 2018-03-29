#!/home/hmsjwzb/python/bin/python3
from StdIn import StdIn

from Sort import Sort

class Heapsort(Sort):
    @staticmethod
    def sort(a):
        N = len(a)-1
        for k in range(N//2, 0, -1):
            Heapsort.sink(a, k, N)
        while N > 1:
            Heapsort.exch(a, 1, N)
            N -= 1
            Heapsort.sink(a, 1, N)

    @staticmethod
    def sink(a, k, N):
        while k*2 <= N:
            j = 2 * k
            if j < N and a[j] < a[j+1]: j += 1
            if not a[k] < a[j]:
                break
            Heapsort.exch(a, k, j)
            k = j

    @staticmethod
    def exch(a, i, j):
        a[i], a[j] = a[j], a[i]

if __name__ == '__main__':
    StdIn = StdIn()
    a = [None]
    a_input = StdIn.readAllStrings()
    a = a + a_input
    Heapsort.sort(a)
    a.pop(0)
    Heapsort.show(a)
