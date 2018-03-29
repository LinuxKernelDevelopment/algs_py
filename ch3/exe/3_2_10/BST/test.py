#!/home/hmsjwzb/python/bin/python3

from BST import BST
from StdIn import StdIn

if __name__ == '__main__':
    st = BST()
    i = 0
    StdIn = StdIn()
    while not StdIn.isEmpty():
        key = StdIn.readString()
        i += 1
        st.put(key, i)

    ##print(st.select(3))
    print(st.rank('L'))
    print(st.height())

    for s in st.keys():
        print(s + " " + str(st.get(s)))
