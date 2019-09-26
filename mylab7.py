def test1():
    line=[1,2,"The",4,(5,6),7,8,"of"]
    print("a) line[5] = ", line[5])
    print("b) line[5:] = ", line[5:8])
    print("c) line[0:5]+line[5:10] = ", line[0:5]+line[5:10])
    print("d) line[:5]+line[5:] = ", line[:5]+line[5:])
    print("e) line[-2] = ", line[-2])
    print("f) lineline[0:10:2] = ", line[0:10:2])
    print("g) line[0:10:-2] = ", line[0:10:-2])
    print("h) line[10:0] = ", line[10:0])
    print("i) line[:] = ", line[:])
    print("j) line[-1:-10:-1] = ", line[-1:-10:-1])
    print("k) line[::-1] = ", line[::-1])
    print("l) line[-1:-10:-3] = ", line[-1:-10:-3])

def test2():
    seq1=(1,2,3,4,5)
    seq2=(6,7,8,9,10)
    seq3=[11,12,13,14,15]
    n=2
    for x in seq1:    #Returns all of the values of x as it becomes each value in the sequence
        print("a) x in seq = ",x)
    print("c) seq1+seq2 = ",seq1+seq2) #Returns seq1 and seq2 in one tuple
    print("d) seq * n = ",seq3*n)    #Returns seq3 n times in one list
    print("e) min(seq) = ",min(seq1)) #Returns the smallest number in the tuple seq1
    print("f) max(seq) = ",max(seq1)) #Returns the largest number in the tuple seq1

    print("*!*!*!*!*!*!*!*!*!*!*!*M*A*S*H*!*!*!*!*!*!*!*!*")
    print("Second part of the assignment")
    mseq=[1,3,5,7,9]
    mseq2=[1,3,5,7,9]
    mseq3=[1,3,5,7,9]
    mseq4=[1,3,5,7,9]
    mseq5=[1,3,5,7,9]
    mseq6=[1,3,5,7,9]
    mseq7=[1,3,5,7,9]
    mseq8=[1,3,5,7,9]
    mseq9=[1,3,5,7,9]
    x=[2,4,6,8]
    x2=[2,4,6,8]
    x3=3
    x4=7
    x5=14
    x6=5
    i=15
    i2=3
    mseq.append(x) #Adds the second list as the last component of the first list
    print("a) mseq.append(x) = ",mseq) 
    mseq2.extend(x2) #Adds the components of the second list as more components of the first list
    print("b) mseq.extend(x) = ",mseq2)
    print("c) mseq.count(x) = ", mseq3.count(x3))#Counts the number of x3(which is 3) in the list
    print("d) mseq.index(w) = ",mseq4.index(x4)) #Returns which place in the list x4(which is 7) resides
    print("e) mseq.insert(i,x) = ",mseq5.insert(i,x5)) #no value returned
    print("f) mseq.pop() = ",mseq6.pop()) #removes and returns the last element
    print("g) mseq.pop(i) = ",mseq7.pop(i2)) #removes and returns the-th element
    mseq8.remove(x6) #removes the first occurence of x6(which is 5)
    print("h) mseq.remove(x) = ",mseq8)
    mseq9.reverse() #reverses in place
    print("i) mseq.reverse() = ",mseq9)
    mseq9.sort() #sorts in place
    print("j) mseq.sort() = ",mseq9)

def test3():
    file=open("E:/CS177/bmi2.py", "r")
    file2=open("E:/CS177/bmi2.py","r")
    file3=open("E:/CS177/bmi2.py","r")
    file4=open("E:/CS177/bmi2.py","r")
    print("file.read() = ")
    print(file.read()) #returns entire file as a string
    print("******************************************************************")
    print("file.readline() = ")
    print(file2.readline()) # returns the next line (new line kept)
    print("******************************************************************")
    print("file.readlines() = ")
    print(file3.readlines()) #returns all the lines in a file as a list of strings (new lines kept)
    print("******************************************************************")
    #line = str(file4.read())
    #line2=line.upper()
    #print(line2[::-1])
    print("******************************************************************")
