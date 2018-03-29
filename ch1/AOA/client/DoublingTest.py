#!/home/hmsjwzb/python/bin/python3
import sys
import random
from Stopwatch import Stopwatch

def timeTrial(N):
    sys.path.append("../ThreeSum/")
    import ThreeSum
    a = [None] * N
    for i in range(N):
        a[i] = random.randint(-1000000, 1000000)
    timer = Stopwatch()
    cnt = ThreeSum.count(a)
    return timer.elapsedTime()

if __name__ == '__main__':
    N = 250
    while True:
        time = timeTrial(N)
        print(str(N) + ' ' + str(time))
        N += N

