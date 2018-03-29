#!/home/hmsjwzb/python/bin/python3
import hashlib

class MyStr:
    def __init__(self, Str):
        self.Str = Str

    def hashCode(self):
        return int(hashlib.sha1(self.Str.encode()).hexdigest(), 16)

    def equals(self, Str):
        return self.Str == Str.Str
