#!/home/hmsjwzb/python/bin/python3.5

from sys import stdin

class StdIn:
    def __init__(self):
        self.myin = stdin()

    def isEmpty(self):
        pass

    def hasNextLine(self):
        pass

    def hasNextChar(self):
        pass

    def readLine(self):
        try:
            line = self.myin.readline()
        except Exception:
            line = None
        return line

    def readChar(self):
        try:
            ch = self.myin.next()
            return char(ch)
        except Exception:
            raise Exception("attempts to read a 'char' value from standard input, but there are no more tokens available")

    def readAll(self):
        try:
            return self.myin.readlines()
        except Exception:
            raise Exception("attempts to read all reminder value from standard input, but there are no more")

    def readString(self):
        try:
            return self.myin.next()
        except Exception:
            raise Exception("attempts to read a 'String' value from standard input, but there are no more tokens available")

    def readInt(self):
        try:
            return int(self.myin.next())
        except Exception:
            raise Exception("attemps to read an 'int' value from standard input, but there are no more tokens available")

    def readDouble(self):
        try:
            ret = float(self.myin.next())
        except Exception:
            raise Exception("attemps to read an 'double' value from standard input, but there are no more tokens available")


    def readFloat(self):
        try:
            return float(self.myin.next())
        except Exception:
            raise Exception("attemps to read an 'float' value from standard input, but there are no more tokens available")


    def readLong(self):
        try:
            return long(self.myin.next())
        except Exception:
            raise Exception("attemps to read an 'int' value from standard input, but there are no more tokens available")

    def readShort(self):
        try:
            return int(self.myin.next())
        except Exception:
            raise Exception("attemps to read an 'short' value from standard input, but there are no more tokens available")

    def readByte(self):
        try:
            return int(self.myin.next())
        except Exception:
            raise Exception("attemps to read an 'int' value from standard input, but there are no more tokens available")

if __name__ == '__main__':
    print("Type a double: ")
    mystdin = StdIn()
    c = mystdin.readDouble()
    print("Your double was: " + str(c))
