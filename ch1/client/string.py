#!/home/hmsjwzb/python/bin/python3

from stack import stack

if __name__ == '__main__':
    s = stack()
    while True:
        try:
            instring = input()
        except EOFError:
            break
        if not instring == '-':
            s.push(instring)
        elif not s.isEmpty():
            print(str(s.pop()) + " ")
    print('(' + str(s.size()) + " left on stack)")
