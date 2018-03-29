#!/home/hmsjwzb/python/bin/python3

#from Scanner import Scanner
import sys

class In:
    def __init__(self, filename, delimiter):
        if delimiter == None:
            self.items = open(filename, 'r').read().split()
        else:
            self.items = open(filename, 'r').read().split(delimiter)

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.items.pop(0)
            return result
        except IndexError:
            raise StopIteration

    def readAllInts(self):
        results = list(map(int, self.items))
        return results

    def readInt(self):
        tmp = next(self)
        return int(tmp)

    def readString(self):
        return str(next(self))

    def readDouble(self):
        return float(next(self))

    def readLine(self):
        return str(next(self))

    def hasNextLine(self):
        return len(self.items) != 0
