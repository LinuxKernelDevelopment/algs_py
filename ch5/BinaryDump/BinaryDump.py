#!/usr/bin/python

from BinaryStdIn import BinaryStdIn
import sys

class BinaryDump:
    def __init__(self):
        pass


if __name__ == '__main__':
    Bin = BinaryStdIn()
    bitsPerLine = 16
    if len(sys.argv) == 2:
        bitsPerLine = int(sys.argv[1])
    count = 0
    str = ""
    while not Bin.isEmpty():
        if bitsPerLine == 0:
            Bin.readBoolean()
            continue
        elif count != 0 and count % bitsPerLine == 0:
            str += "\n"
        if Bin.readBoolean(): str += '1'
        else:               str += '0'
        count += 1
    if bitsPerLine != 0: str += '\n'
    str += "%d bits" % (count)
    print(str)

