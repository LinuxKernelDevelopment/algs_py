#!/home/hmsjwzb/python/bin/python3.6
import sys
sys.path.append("/home/hmsjwzb/intel/Algorithm/tools")
from StdIn import StdIn

BITS_PER_BYTE = 8

class LSD:
    def __init__(self):
        pass

    def sort_2(self, a, w):
        n = len(a)
        R = 256
        aux = [None] * n

        for d in range(w-1, -1, -1):

            count = [0] * (R+1)
            for i in range(0, n):
                count[ord(a[i][d]) + 1] += 1

            for r in range(0, R):
                count[r+1] += count[r]

            for i in range(0, n):
                aux[count[ord(a[i][d])]] = a[i]
                count[ord(a[i][d])] += 1
            for i in range(0, n):
                a[i] = aux[i]

    def sort_1(self, a):
        BITS = 32
        R = 1 << BITS_PER_BYTE
        MASK = R - 1
        w = BITS / BITS_PER_BYTE

        n = len(a)
        aux = [0] * n

        for d in range(0, w):
            count = [0] * (R + 1)
            for i in range(0, n):
                c = (a[i] >> BITS_PER_BYTE*d) and MASK
                count[c + 1] += 1

            for r in range(0, R):
                count[r+1] += count[r]

            if d == w - 1:
                shift1 = count[R] - count[R/2]
                shift2 = count[R/2]
                for r in range(0, R/2):
                    count[r] += shift1
                for r in range(R/2, R):
                    count[r] -= shift2

            for i in range(0, n):
                c = (a[i] >> (BITS_PER_BYTE * d)) & MASK
                count[c] += 1
                aux[count[c]] = a[i]

            a = aux

if __name__ == '__main__':
    myin = StdIn()
    a = myin.readAllStrings()
    n = len(a)

    mylsd = LSD();
    w = len(a[0])
    for i in range(0, n):
        assert len(a[i]) == w, "Strings must have fixed length"

    mylsd.sort_2(a, w)

    for i in range(0, n):
        print(a[i])
