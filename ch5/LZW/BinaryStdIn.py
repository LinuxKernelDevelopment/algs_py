#!/usr/bin/python
import sys
from BinaryStdOut import BinaryStdOut

class BinaryStdIn:
    def __init__(self):
        self.isInitialized=False
        pass

    def initialize(self):
        self.fin = open("/dev/stdin", "rb")
        self.buffer = 0
        self.n = 0
        self.fillBuffer()
        self.isInitialized = True
        self.EOF = False

    def fillBuffer(self):
        self.buffer = self.fin.read(1)
        self.n = 8
        if not self.buffer:
            #print("EOF")
            self.EOF = True
            self.n = -1

    def close(self):
        if not self.isInitialized:
            self.initialize()
        self.isInitialized = False

    def isEmpty(self):
        if not self.isInitialized:
            self.initialize()
        return self.EOF == True


    def readBoolean(self):
        if self.isEmpty():
            #raise ValueError("Reading from empty input stream")
            return None
        self.n -= 1
        bit = ((int.from_bytes(self.buffer, byteorder=sys.byteorder) >> self.n) & 1) == 1
        if self.n == 0:
            self.fillBuffer()
        return bit

    def readChar(self):
        if self.isEmpty():
            raise ValueError("Reading from empty input stream")

        if self.n == 8:
            x = self.buffer
            self.fillBuffer()
            #print(x)
            return int.from_bytes(x, byteorder=sys.byteorder) & 0xff
        x = int.from_bytes(self.buffer, byteorder=sys.byteorder) & 0xff
        x <<= (8 - self.n)
        oldN = self.n
        self.fillBuffer()
        if self.isEmpty():
            raise ValueError("Reading from empty input stream")
        self.n = oldN
        x |= (int.from_bytes(self.buffer, byteorder=sys.byteorder) >> self.n)
        return (x & 0xff)


    def readChar_r(self, r):
        if r < 1 or r > 16:
            raise TypeError("Illegal value r = %d\n" % (r))
        if r == 8:
            return self.readChar()

        x = 0
        for i in range(i, r):
            x << 1
            bit = self.readBoolean()
            if bit:
                x |= 1
        return x

    def readString(self):
        if self.isEmpty():
            raise ValueError("Reading from empty input stream")
        sb = ""
        while not self.isEmpty():
            c = self.readChar()
            sb += chr(c)
        return sb

    def readShort(self):
        x = 0
        for i in range(0, 2):
            c = self.readChar()
            x <<= 8
            x |= c
        return x

    def readInt(self):
        x = 0
        for i in range(0, 4):
            c = self.readChar()
            x <<= 8
            x |= c
        return x

    def readInt_r(self, r):
        if self.isEmpty():
            return None
        if r < 1 or r > 32:
            raise ValueError("Illegal value of r = %d" % (r))
        if r == 32:
            return self.readInt()
        x = 0
        for i in range(0, r):
            x <<= 1
            bit = self.readBoolean()
            if bit:
                x |= 1
        return x

    def readLong(self):
        x = 0
        for i in range(0, 8):
            c = self.readChar()
            x <<= 8
            x |= c
        return x

    def readDouble(self):
        return struct.unpack("d", self.readLong())

    def readFloat(self):
        return struct.unpack("f", self.readInt())

    def readByte(self):
        c = self.readChar()
        return c & 0xff

if __name__ == '__main__':
    Bin = BinaryStdIn()
    Bout = BinaryStdOut()
    while not Bin.isEmpty():
        c = Bin.readChar()
        Bout.writeByte(c)
