#!/home/hmsjwzb/python/bin/python3

class Mystr(str):
    def __new__(cls, *args, **kw):
        return str.__new__(cls, *args, **kw)

    def compareto(self, strb):
        if self.
