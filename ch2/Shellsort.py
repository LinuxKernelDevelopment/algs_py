#!/home/hmsjwzb/python/bin/python3

from Sort import Sort
class Shell(Sort):
    @staticmethod
    def sort(a):
        N = len(a)
        h = 1
        while h < N/3: h = 3 * h + 1
        while h >= 1:
            for i in range(h, N):
                for j in range(i, h-1, -h):
                    if Shell.less(a[j], a[j-h]):
                        Shell.exch(a, j, j-h)
            h = h//3
    


if __name__ == '__main__':
    a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    Shell.sort(a)
    Shell.show(a)
