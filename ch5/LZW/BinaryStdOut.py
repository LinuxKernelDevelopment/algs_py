#!/usr/bin/python
import sys
import struct

class BinaryStdOut:
    def __init__(self):
        self.isInitialized = False
        pass

    def initialize(self):
        self.out = open("/dev/stdout", "wb")
        self.buffer = 0
        self.n = 0
        self.isInitialized = True

    def writeBit(self, bit):
        if not self.isInitialized:
            self.initialize()

        #print(self.buffer, bit)
        self.buffer <<= 1
        if bit:
            self.buffer |= 1

        self.n += 1
        #print(self.n)
        if self.n == 8:
            self.clearBuffer()

    def writeByte(self, x):
        #print("x:" + str(x))
        if not self.isInitialized:
            self.initialize()

        assert x >= 0 and x < 256

        '''if self.n == 0:
            self.out.write(x.to_bytes(1, sys.byteorder))
            return'''

        for i in range(0, 8):
            bit = (((x >> (8 - i -1)) & 1) == 1)
            self.writeBit(bit)

    def clearBuffer(self):
        if not self.isInitialized:
            self.initialize()

        if self.n == 0:
            return
        if self.n > 0:
            self.buffer <<= (8 - self.n)
        #print(self.buffer.to_bytes(1, sys.byteorder),file=sys.stderr)
        self.out.write(struct.pack('B', self.buffer))
        self.n = 0
        self.buffer = 0

    def flush(self):
        self.clearBuffer()

    def close(self):
        self.out.close()
        self.isInitialized = False

    def write_b(self, x):
        self.writeBit(x)

    def write_B(self, x):
        self.writeByte(ord(x) & 0xff)

    def write_i(self, x):
        self.writeByte((x >> 24) & 0xff)
        self.writeByte((x >> 16) & 0xff)
        self.writeByte((x >>  8) & 0xff)
        self.writeByte((x >>  0) & 0xff)

    def write_i_r(self, x, r):
        if r == 32:
            self.write_i(x)
        if r < 1 or r >32:
            raise ValueError("Illegal value for r = %d" %(r))
        if x < 0 or x >= (1 << r):
            raise ValueError("Illegal %d -bit char = " % (x))
        for i in range(0, r):
            bit = ((x >> (r - i - 1)) & 1) == 1
            self.write_b(bit)

    def write_c(self, x):
        if ord(x) < 0 or ord(x) >= 256:
            raise ValueError("Illegal 8-bit char = %c" % (x))
        self.write_B(x)

    def write_S(self, s):
        for i in s:
            self.write_c(i)

if __name__ == '__main__':
    Bout = BinaryStdOut()
    m = int(sys.argv[1])

    for i in range(64, 101):
        Bout.write_i(i)
    Bout.flush()





