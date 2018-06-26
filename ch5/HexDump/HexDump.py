#!/usr/bin/python
import sys
from BinaryStdIn import BinaryStdIn

if __name__ == '__main__':
    bytesPerLine = 16
    Bin = BinaryStdIn()
    if len(sys.argv) == 2:
        bytesPerLine = int(sys.argv[1])

    i = 0
    str = ""
    while not Bin.isEmpty():
        if bytesPerLine == 0:
            Bin.readChar()
            continue
        if i == 0:
            str += ""
        elif i % bytesPerLine == 0:
            str += "\n%d" % (i)
        else:
            str += " "
        c = Bin.readChar()
        str += ("%02x" % (c & 0xff))
        i += 1
    if bytesPerLine != 0:
        str += "\n"
    print(str)
    print("%d bits" % (i * 8))
