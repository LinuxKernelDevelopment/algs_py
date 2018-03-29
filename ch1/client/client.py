#!/home/hmsjwzb/python/bin/python3

from Bag import Bag
from StdIn import StdIn
from math import sqrt

if __name__ == '__main__':
    In = StdIn()
    numbers = Bag()

    while not In.isEmpty():
        numbers.add(In.readDouble())

    N = numbers.size()
    sum = 0
    for x in numbers:
        sum += x

    mean = sum / N

    sum = 0.0
    for x in numbers:
        sum += (x - mean) * (x -mean)

    std = sqrt(sum / (N - 1))

    print("Mean: " + str(mean) + '\n')
    print("Std dev:" + str(std) + '\n')
