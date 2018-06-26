#!/bin/python
import sys

class BinaryDump:
    def __init__(self):
        pass

    def dump(self, args):
        mstr = ""
        count = 0
        bytesPerLine = 16
        if len(args) == 1:
            bytesPerLine = int(args[1])
        data = sys.stdin.buffer.read()
        i = 0
        for item in data:
            if i == 0:
                print("")
            if bytesPerLine == 0:
                continue
            if i % bytesPerLine == 0:
                mstr += "\n"
            else:
                mstr += " "
            mstr += str(format(item, '2x'))
            i += 1
        mstr += "\n" + "%d bits" % (i * 8)
        print(mstr)


if __name__ == '__main__':
    f = BinaryDump()
    f.dump(sys.argv)
