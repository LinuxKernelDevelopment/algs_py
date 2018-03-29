#!/home/hmsjwzb/python/bin/python3
import sys
import random
from Stopwatch import Stopwatch

if __name__ == '__main__':
    sys.path.append("../ThreeSum/")
    import ThreeSum
    N = int(sys.argv[1])
    a = [None] * N
    for i in range(N):
        a[i] = random.randint(-1000000, 1000000)
    timer = Stopwatch()
    cnt = ThreeSum.count(a)
    time = timer.elapsedTime()
    print(str(cnt) + " triples " + str(time))

