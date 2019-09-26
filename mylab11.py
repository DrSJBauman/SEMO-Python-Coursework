import pickle
import random
import os
import string
os.getcwd()
s="E:\\CS177"
os.chdir(s)
def code(string):
    L=[]
#For each character in the string, gets the cooresponding ASCII code and adds
#it to a list
    for i in string:
        code=ord(i)
        L.append(code)
    return(L)

def unicodeconvert(listofunicode):
#For each unicode character given, returns its value
    for i in listofunicode:
        j=chr(ord(i))
        print(j)

def encode(string):
    newstring=''
#Opens a file for writing the coded message into
    fout=open('coded','wb')
#For each character in the string, changes the designated ones to their
#cooresponding characters and pickles the new string to a file
    for i in string:
        if i=='a':
            newstring+='d'
        elif i=='b':
            newstring+='e'
        elif i=='e':
            newstring+='f'
        elif i=='u':
            newstring+='x'
        elif i=='v':
            newstring+='y'
        elif i=='w':
            newstring+='z'
        elif i=='x':
            newstring+='a'
        elif i=='y':
            newstring+='b'
        elif i=='z':
            newstring+='c'
        else: newstring+=i
    pickle.dump(newstring,fout)
    return(newstring)

def decode():
    newstring=''
#Opens the file from the above function for reading
    j=open('coded','rb')
#Loads the pickled encoded message from the above function
    G=pickle.load(j)
#For the characters that changed in the above function, changes them back the
#reverse way...doesn't work necessarily due to poor coding methods
#(z was changed to c,and d-a but c wasn't changed so the decoded message is wrong)
    for i in str(G):
        if i=='d':
            newstring+='a'
        elif i=='e':
            newstring+='b'
        elif i=='f':
            newstring+='e'
        elif i=='x':
            newstring+='u'
        elif i=='y':
            newstring+='v'
        elif i=='z':
            newstring+='w'
        elif i=='a':
            newstring+='x'
        elif i=='b':
            newstring+='y'
        elif i=='c':
            newstring+='z'
        else: newstring+=i
    return(newstring)


def codekey():
#Creates a random code key for the lowercase letters a through z using ASCII codes
    L=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Lis=[]
    randli=[]
    fout=open('coded2','wb')
    ox={}
    yn2=0
    yn=0
#For the letters in the list, L, makes the letter into the cooresponding ASCII number
    for i in L:
        li=ord(i)
        yn=0
#Picks a random integer between 97 and 122 while the check, yn, is zero
        while yn == 0:
            n=random.randint(97,122)
#While the ASCII number cooresponding to the letter is equal to the random
#number that was chosen, it picks a different random number in the same range
            while n == li:
                n=random.randint(97,122)
            yn2=0
#Runs through the list, randli, and if the random number chosen is the same as
#any number in the list, it makes the check yn2 equal one so that the first while
#loop will keep running, as yn will still be zero
            for j in randli:
                if n == j:
                    yn2=1
            if yn2 == 1:
                yn=0
            else: yn=1
#If the random number chosen is not in the list, randli, already and is not the
#same as the ASCII code that already cooresponds to the letter, it adds the
#number to randli
        randli.append(n)
#Creates a dictionary with the string of the i'th value in the list, L, as the key
#and the i'th value in randli as the value
    for i in range(0,26):
        ox[str(L[i])]=randli[i]
#Dumps the dictionary(which is now the code key) to the file, fout
    pickle.dump(ox,fout)

def stringencode(strng,codekey):
#Encodes a given string using a given code key that was saved in a previous file
    s=""
#Makes the given string all lowercase
    strng=strng.lower()
#Opens the given file that contains the code key
    fin=open(codekey,'rb')
    ox=pickle.load(fin)
#Runs through the string and makes the characters into their ASCII numbers
    for i in strng:
        n=ord(i)
#If the ASCII number is within 97 to 122
        if n >=97 and n<=122:
#Makes the value of i in the dictionary equal to n
            n=ox[i]
#Finds the ASCII character the new n value
            c=chr(n)
#If the ASCII number wasn't in 97 to 122, it remains the same as it was typed in
        else: c=i
#Adds the changed values of the characters to a new string and prints that
        s=s+c
    return(s)

def stringdecode(encodedstrng, codekey):
#Decodes a given encoded string in the reverse manner than the encode function above
#Must use the same code key as the encode function above used if they are to be
#used together
    s=''
    ox2={}
    fin=open(codekey,'rb')
    ox=pickle.load(fin)
#For the keys in the codekey dictionary, switches the keys and values to values and keys
    for key in ox:
        ox2[ox[key]]=key
#For the characters in the encoded string, finds the ASCII numbers of each and
#finds the value of each, which is the key in the switched around dictionary
    for i in encodedstrng:
        n=ord(i)
        c=ox2.get(n,i)
#Makes a new string with the given string decoded
        s=s+c
    print(s)
        
def anagram():
    s=""
    strng=input("Enter a message to be encoded: ")
#Makes the given string all lowercase
    strng=strng.lower()
#Opens the file, coded2, which contains the code key
    fin=open('coded2','rb')
    ox=pickle.load(fin)
#Runs through the string and makes the characters into their ASCII numbers
    for i in strng:
        n=ord(i)
#If the ASCII number is within 97 to 122
        if n >=97 and n<=122:
#Makes the value of i in the dictionary equal to n
            n=ox[i]
#Finds the ASCII character the new n value
            c=chr(n)
#If the ASCII number wasn't in 97 to 122, it remains the same as it was typed in
        else: c=i
#Adds the changed values of the characters to a new string and prints that
        s=s+c
    print(s)

def anagramdecode():
    encodedstrng=input("Enter your anagram to decode: ")
    s=''
    ox2={}
    fin=open('coded2','rb')
    ox=pickle.load(fin)
#For the keys in the coded2 dictionary, switches the keys and values to values and keys
    for key in ox:
        ox2[ox[key]]=key
#For the characters in the encoded string, finds the ASCII numbers of each and
#finds the value of each, which is the key in the switched around dictionary
    for i in encodedstrng:
        n=ord(i)
        c=ox2.get(n,i)
#Makes a new string with the given string decoded
        s=s+c
    return(s)


def letterfrequency(text):
#Returns the frequency of the characters in a text file
    fin=open(text,'r')
    ox={}
#Makes the characters lowercase, and for each character in the file,
#adds it to the dictionary as the key and counts its occurances as the value
    for ch in fin.read().lower():
        ox[ch]=ox.get(ch,0)+1
#Switches the keys and  values of the dictionary
    items=[(v,k) for k, v in ox.items()]
#Sorts the keys(which are now the numbers) smallest to largest
    items.sort()
#Reverses the list so that the numbers are largest to smallest
    items.reverse()
#Switches the keys and values back and prints the list of letters and frequencies
    items=[(k,v) for v,k in items]
    return(items)

def shortwordfrequency(text):
#Returns the frequencies of one, two, and three letter words in a text file
    fin=open(text,'r')
    ox={}
#For each line in the file, splits the words up and if the word is less than four
#characters long, adds it and its count to the dictionary
    for line in fin.readlines():
        line.lower()
        line=line.split()
        for wd in line:
            if len(wd)<4:
                ox[wd]=ox.get(wd,0)+1
#Sorts the dictionary as a list, with the frequencies going from biggest to smallest
    items=[(v,k) for k, v in ox.items()]
    items.sort()
    items.reverse()
    items=[(k,v) for v,k in items]
    return(items)
