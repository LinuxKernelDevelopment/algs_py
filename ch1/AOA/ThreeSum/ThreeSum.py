#!/home/hmsjwzb/python/bin/python3
import sys
from In import In

def count(a):
    N = len(a)
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if a[i] + a[j] + a[k] == 0:
                    cnt += 1
    return cnt

if __name__ == '__main__':
    myin = In(sys.argv[1])
    a = myin.readAllInts()
    print(count(a))



