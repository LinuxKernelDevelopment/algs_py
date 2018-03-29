#!/home/hmsjwzb/python/bin/python3
from Stopwatch import Stopwatch
import sys
import random
from MyInsertion import Insertion
from Selection import Selection
from Shellsort import Shell

class SortCompare:
    def time(alg, a):
        timer = Stopwatch()
        if alg == "Insertion": Insertion.sort(a)
        if alg == "Selection": Selection.sort(a)
        if alg == "Shell":     Shell.sort(a)
        return timer.elapsedTime()

    def timeRandomInput(alg, N, T):
        total = 0
        a = [None] * N 
        for t in range(0, T):
            for i in range(0, N):
                a[i] = random.randint(-1000000, 1000000)
            total += SortCompare.time(alg, a)
        return total

if __name__ == '__main__':
    alg1 = sys.argv[1]
    alg2 = sys.argv[2]
    N = int(sys.argv[3])
    T = int(sys.argv[4])
    t1 = SortCompare.timeRandomInput(alg1, N, T)
    t2 = SortCompare.timeRandomInput(alg2, N, T)
    print("For %d random Doubles\n %s is" % (N, alg1))
    print("%.1f times faster than %s\n" % (t2/t1, alg2))


