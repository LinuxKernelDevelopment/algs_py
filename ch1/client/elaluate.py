#!/home/hmsjwzb/python/bin/python3

from stack import stack
from math import sqrt
from decimal import Decimal

def evaluate():
    ops = stack()
    vals = stack()
    inline = input().split()
    for s in inline:
        if s == '(': pass
        elif s == '+': ops.push(s)
        elif s == '-': ops.push(s)
        elif s == '*': ops.push(s)
        elif s == '/': ops.push(s)
        elif s == 'sqrt': ops.push(s)
        elif s == ')':
            op = ops.pop()
            v = vals.pop()
            if op == '+': v = float(vals.pop()) + v
            elif op == '-': v = float(vals.pop()) - v
            elif op == '*': v = float(vals.pop()) * v
            elif op == '/': v = float(vals.pop()) / v
            elif op == 'sqrt': v = sqrt(v)
            vals.push(v)
        else:
            vals.push(float(s))
    print(str(vals.pop()))

if __name__ == '__main__':
    evaluate()
