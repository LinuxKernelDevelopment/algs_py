#!/home/hmsjwzb/python/bin/python3
import sys
from In import In
from BinarySearch import BinarySearch

def count(a):
    a.sort()
    N = len(a)
    cnt = 0
    for i in range(N):
        if BinarySearch.rank(-a[i], a) > i:
            cnt += 1
    return cnt

if __name__ == '__main__':
    myin = In(sys.argv[1])
    a = myin.readAllInts()
    print(count(a))



