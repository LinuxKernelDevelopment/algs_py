#!/home/hmsjwzb/python/bin/python3

class Scanner:
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        in_list = input().split()
        while True:
            return in_list.pop(0)
            in_list = input()

    def hasNext(self):


