#!/home/hmsjwzb/python/bin/python3

class Mychar(str):
    def __new__(cls, *args, **kw):
        return str.__new__(cls, *args, **kw)

    def compareTo(self, other):
        result = ord(self[0]) - ord(other[0])
        if result > 0:
            return 1
        elif result < 0:
            return -1
        else:
            return 0

if __name__ == '__main__':
    a = Mychar('C')
    b = Mychar('A')
    print(a.compareTo(b))
