import binascii
import json
import sys
import numpy
import zlib
import pickle


def main():
    mydict = None
    fileToWrite = sys.argv[2]
    fileToRead = sys.argv[1]

    file = open(fileToWrite, "wb")
    fileRead = open(fileToRead, "rb")

    data = fileRead.read()
    head = 2
    ahead = 0
    dictInterval = 0

    while mydict is None:
        search = data[ahead:head]
        search = search.decode('latin1')

        if search == '\n\n':
            mydict = data[dictInterval:head]
            mydict = dict2File(mydict)
            #mydict = json.loads(mydict)
            print(mydict)
            break
        head = head + 1
        ahead = ahead + 1
    searchb = 0
    searchIterator = 0
    datab = data[head:(len(data))]
    st =''
    array = []

    for char in datab:
        st += bin(ord(chr(char)))[2:].zfill(7)
    print(st)
    letter = ""
    while searchb in range(len(st)):
        searchBuffer = st[searchIterator:searchb]
        stringBuffer = searchBuffer

        if stringBuffer in mydict:
            print(mydict[stringBuffer])
            letter += str(mydict[stringBuffer])

            searchIterator = searchb;

        searchb = searchb + 1
    a = 0
    while a in range(len(letter)):
        while len(array)<8 and a<len(letter):
            array.append(int(letter[a]))
            a=a+1
        print(array)
        char = bytearray(numpy.packbits(array)).decode('latin1')
        print(char)
        byte = bytes(char, 'latin1')
        file.write(byte)
        array.clear()
    fileRead.close()
    file.flush()
    file.close();

def dict2File(file):
    bytes = zlib.decompress(file)
    return pickle.loads(bytes)

main()