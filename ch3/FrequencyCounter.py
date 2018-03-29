#!/home/hmsjwzb/python/bin/python3
from StdIn import StdIn
import sys
from SequentialSearchST import SequentialSearchST
from BinarySearchST import BinarySearchST

if __name__ == '__main__':
    minlen = int(sys.argv[1])
    StdIn = StdIn()
    st = BinarySearchST()
    while not StdIn.isEmpty():
        word = StdIn.readString()
        if len(word) < minlen:
            continue
        if not st.contains(word):
            st.put(word, 1)
        else:
            st.put(word, st.get(word) + 1)

    max = ""
    st.put(max, 0)
    for word in st.Keys(0, len(st.keys)):
        if st.get(word) > st.get(max):
            max = word
    print(max + " " + str(st.get(max)))
