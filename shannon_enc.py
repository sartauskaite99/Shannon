import json
import sys; print(sys.executable)
import numpy


def encoder():
    fileToRead = sys.argv[1]
    fileToWrite = sys.argv[2]
    lenghtOfWord = sys.argv[3]
    file1 = numpy.fromfile(fileToRead, dtype = "uint8")
    file = numpy.unpackbits(file1)
    print(file1)
    file2 = open(fileToWrite, 'wb')
    number = int(lenghtOfWord)
    List = []
    List = getList(file, number)
    frequency = calculateFrequency(List)
    sortedFrequency = sorted(frequency.items(), key=lambda item: item[1],reverse=True)
    total = len(file1)
    lenght = lenghtOfBinarySymbols(sortedFrequency, total)
    binary = binaryAlphabet(lenght, sortedFrequency, total)
    file2 = writeToFile(List,binary,file2, number)

    file2.close()
    
def calculateFrequency(file):
    frequency = {}
    for character in file:
        if not character in frequency:
            frequency[character] = 0
        frequency[character] += 1
    return frequency

def lenghtOfBinarySymbols(data, total):
    lenght = []
    size = len(data)
    for i in range(size):
        count = 0
        probability = data[i][1]
        while probability < total:
            probability = probability*2
            count += 1
        lenght.append(count)
    return lenght

def binaryAlphabet(lenght, data, total):
    alphabet = {}
    size = len(data)
    for i in range(size):
        probability = data[i][1]

        symbol = data[i][0]
        binary = ''
        if i == 0:
            binary = decimalToBinary(0, lenght[i])
            alphabet[symbol] = binary
            number = data[i][1]
        else:
            decimalNumber = number/total
            binary = decimalToBinary(decimalNumber, lenght[i])
            number = number + data[i][1]
        alphabet[symbol] = binary
        
    return alphabet

def decimalToBinary(number, lenght):
    binary = ''
    for i in range(lenght):
        number = number * 2
        if number >= 1:
            binary += '1'
            number = number - 1
        else:
            binary += '0'
    return binary

def reverseValues(dictionary):
    new_dict = {}
    for k, v in dictionary.items():
        new_dict[v] = k
    return new_dict

def writeToFile(file, dictionary,file2, number):
    reverseBinary = reverseValues(dictionary)
    print(reverseBinary)
    s = json.dumps(reverseBinary)
    file2.write(bytes(s.encode()))
    line = '\n\n'
    file2.write(line.encode('utf-8'))
    for i in file:
        for key in dictionary:
            if i == key:
                # bytes = numpy.packbits((dictionary[key]).encode())
                # bytes.tofile(file2)
                file2.write(bytes((dictionary[key]).encode()))

    return file2

def getList(data, number):
    a = ''
    lis = []
    x = 0
    for i in data:
        x += 1
        a += str(i)
        if(x>len(data)-(len(data)%number)):
            lis.append(a)
            a=''
        if(x%number==0):
            lis.append(a)
            a=''
        
            
    return lis
            

encoder()