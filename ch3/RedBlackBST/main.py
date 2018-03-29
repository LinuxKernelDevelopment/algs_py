#!/home/hmsjwzb/python/bin/python3
from RedBlackBST import RedBlackBST
from char import Mychar
from StdIn import StdIn

if __name__ == '__main__':
    st = RedBlackBST()
    i = 0
    StdIn = StdIn()
    while not StdIn.isEmpty():
        key = Mychar(StdIn.readString())
        i += 1
        print("put %s" % key)
        st.put(key, i)

    #print(st.select(3))
    #print(st.rank('L'))
    A = Mychar('A')
    S = Mychar('S')

    for s in st.Keys():
        print(s + " " + str(st.get(s)))
        st.delete(s)
