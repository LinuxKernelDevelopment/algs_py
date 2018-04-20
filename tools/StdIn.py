#!/home/hmsjwzb/python/bin/python3

#from Scanner import Scanner
import sys

class StdIn:
    def __init__(self):
        tmp = input()
        self.items = []
        while True:
            self.items += tmp.split()
            self.stop = False
            try:
                tmp = input()
            except EOFError:
                break

    def isEmpty(self):
        #print(self.stop)
        return self.stop

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.items != []:
                result = self.items.pop(0)
                return result
            else:
                tmp = input()
                #print("input:%s" % tmp)
                self.items = tmp.split()
                result = self.items.pop(0)
                return result
        except EOFError:
            self.stop = True
            return False
            #raise RuntimeWarning("new")

    def readInt(self):
        return int(next(self))

    def readString(self):
        return str(next(self))

    def readDouble(self):
        return float(next(self))

    def readAllStrings(self):
        return [str(element) for element in self.items]

    def readLine(self):
        return str(next(self))

    def hasNextLine(self):
        if self.items != None:
            return True
        else:
            tmp = input()
            self.items = tmp.split('\n')
            return True
