#!/home/hmsjwzb/python/bin/python3
from StdIn import StdIn

from Sort import Sort
class Selection(Sort):
    @staticmethod
    def sort(a):
        N = len(a)
        min = a[0]
        for odx, item in enumerate(a):
            min = item
            min_idx = odx
            for idx, min_item in enumerate(a[odx:N]):
                if min_item < min:
                    min_idx = idx + odx
                    min = min_item
            Selection.exch(a, odx, min_idx)

if __name__ == '__main__':
    #a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    StdIn = StdIn()
    a = StdIn.readAllStrings()
    Selection.sort(a)
    Selection.show(a)
