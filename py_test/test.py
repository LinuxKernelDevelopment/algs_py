#!/home/hmsjwzb/python/bin/python3
class MyStr(str):
    def __sub__(self, other):
        for s, o in zip(self, other):
            if ord(s) == ord(o):
                continue
            else:
                return ord(s) - ord(o)
        if len(self) == len(other):
            return 0
        else:
            pos = min(len(self), len(other))
            return self[pos] - self[pos]

if __name__ == '__main__':
    word1 = MyStr("hello")
    word2 = MyStr("hello1")
    print(word1-word2)
