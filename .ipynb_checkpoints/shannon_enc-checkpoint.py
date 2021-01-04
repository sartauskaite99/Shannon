import sys; print(sys.executable)
import numpy


# mydict = {'00': 97, '011': 108, '100': 98, '110': 115}

def main():
    mydict = encoder()
    buffer = 1024
    
    fileToWrite = sys.argv[3]
    fileToRead = sys.argv[2]
    file = open(fileToWrite, "wb")
    fileRead = open(fileToRead, "rb")
    data = fileRead.read()
    
    searchIterator = 0
    head = 0
    value = 0
    
    while head in range(len(data)+1):
        searchBuffer = data[searchIterator:head]
        stringBuffer = searchBuffer.decode()
        if stringBuffer in mydict:
            letter = chr(mydict[stringBuffer])
            byte = bytes(letter, 'utf-8')
#             print(byte)
            file.write(byte)
            searchIterator = head;
        head = head + 1
        
#         if head >= buffer:
#             searchIterator = head - buffer
    print(head)
    fileRead.close()
    file.flush()
    file.close();
    
def encoder():
    fileToRead = sys.argv[1]
    fileToWrite = sys.argv[2]
    lenghtOfWord = sys.argv[3]
    file1 = numpy.fromfile(fileToRead, dtype = "uint8")
    file = numpy.unpackbits(file1)
    file2 = open(fileToWrite, 'wb')
    number = int(lenghtOfWord)
    List = []
    List = getList(file, number)
    frequency = calculateFrequency(List)
    sortedFrequency = sorted(frequency.items(), key=lambda item: item[1],reverse=True)
    total = len(file)
    lenght = lenghtOfBinarySymbols(sortedFrequency, total)
    binary = binaryAlphabet(lenght, sortedFrequency, total)
    file2 = writeToFile(List,binary,file2, number)
    reverseBinary = reverseValues(binary)
    file2.close()
#     file1.close()
    print(reverseBinary)
    return reverseBinary
    
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
        else: binary += '0'
    return binary

def reverseValues(dictionary):
    new_dict = {}
    for k, v in dictionary.items():
        new_dict[v] = k
    return new_dict

def writeToFile(file, dictionary,file2, number):
    for i in file:
        for key in dictionary:
            if i == key:
                file2.write(bytes((dictionary[key]).encode()))
#                 bytes = numpy.packbits((dictionary[key]).encode())
#                 bytes.tofile(file2)
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