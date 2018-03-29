#!/home/hmsjwzb/python/bin/python3

from stack import stack

if __name__ == '__main__':
    s = stack()
    instring = input().split()
    for temp in instring:
        if not temp == '-':
            s.push(temp)
        elif not s.isEmpty():
            print(str(s.pop()) + " ")
    print('(' + str(s.size()) + " left on stack)")
