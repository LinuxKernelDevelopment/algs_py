#!/bin/python
import sys

class BinaryDump:
    def __init__(self):
        pass

    def dump(self, args):
        mstr = ""
        count = 0
        bitsPerLine = 16
        if len(args) == 1:
            bitPerLine = int(args[1])
        data = sys.stdin.buffer.read()
        for item in data:
            count += 1
            mstr += str(format(item, '08b'))
            if bitsPerLine == 0:
                continue
            elif count != 0 and (count * 8) % bitsPerLine == 0:
                mstr += '\n'
        mstr += "%d bits" % (count * 8)
        print(mstr)


if __name__ == '__main__':
    f = BinaryDump()
    f.dump(None)
