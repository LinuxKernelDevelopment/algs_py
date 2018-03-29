#!/home/hmsjwzb/python/bin/python3

from Sort import Sort
class Insertion(Sort):
    def sort(a):
        N = len(a)
        for i, item in enumerate(a):
            j = i
            for inset_item in reversed(a[0:i]):
                if Insertion.less(a[j], a[j-1]):
                    Insertion.exch(a, j, j-1)
                j -= 1
    


if __name__ == '__main__':
    a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    Insertion.sort(a)
    Insertion.show(a)
