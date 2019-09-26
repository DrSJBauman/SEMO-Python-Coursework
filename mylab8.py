import os
os.getcwd()
s="E:\\CS177"
os.chdir(s)
def lorem():
#Reads in a file, counts the number of times each word appears, and prints the
#words and amounts of times associated with them as key-value pairs:

#Opens the file for reading:
    fin=open("E:\\CS177\\LOREM.txt","r")
#Reads in a file line by line:
    line=str(fin.read())
#Replaces the symbols with spaces:
    for ch in '.,!?':
        line=str.replace(line,ch,' ')
#Breaks each line into words:
    L=line.split()
#Creates an empty dictionary, ox:
    ox={}
#Runs through the components of the list, L:
    for wd in L:
#Builds a dictionary of word counts:
        ox[wd]=ox.get(wd,0)+1
#Prints the key value pairs in the dictionary:
    print(ox)
#Closes the file:
    fin.close()

def lorem2():
#Does the same as the above program, but puts only one pair per line
#and writes this into a file:
    
    fin=open("E:\\CS177\\LOREM.txt","r")
    line=str(fin.read())
#Replaces the symbols with spaces:
    for ch in '!@#$%^&*(),.?/;:"[]{}':
#In the book, it is string, and its not built in.We just use str:
        line=str.replace(line,ch,' ') 
    L=line.split()
    ox={}
    for wd in L:
        ox[wd]=ox.get(wd,0)+1
#Opens the file for writing:
    fout=open("E:\\CS177\\writeinmylab8.txt","w")
    fout2=open("E:\\CS177\\forlorem4.txt","w")
#Runs through the keys of ox:
    for key in ox:
#Prints the keys of ox, a comma, and the values of ox:
        #print("(",kv,",",ox[kv],")")
#Writes the key value pairs to the file with commas and parens
#and puts one pair on a line:
        st=str("("+key+", "+str(ox[key])+")"+"\n")
        st2=str(key+" "+str(ox[key])+"\n")
#Writes the string to the file:
        fout.write(st)
        fout2.write(st2)
    fout.close()
    fout2.close()

#Problems: there would be no way to write the pairs as actual
#'key-value pairs' without doing it as a key, and a value
    
def lorem2b():
#Does the same as the above program, but instead of putting one pair
#per line, it puts all of the pairs together, seperated by ! and
#whitespace, and the key and value are seperated by a colon:
    
    fin=open("E:\\CS177\\LOREM.txt","r")
    line=str(fin.read())
    for ch in '!@#$%^&*(),.?/;:"[]{}':
#In the book, it is string, and its not built in.We just use str:
        line=str.replace(line,ch,' ') 
    L=line.split()
    ox={}
    for wd in L:
        ox[wd]=ox.get(wd,0)+1
    fout=open("E:\\CS177\\writeinmylab8.txt","w")
#Runs through the keys of ox
    for key in ox:
#Writes the key value pairs to the file with : ! and whitespace:
        st=str(key+":"+str(ox[key])+"!"+"   ")        
        fout.write(st)
    fout.close()


def lorem3():
#Reads in the file as a string that looks either like lorem2 or lorem2b,
#whichever of the two was run most recently:
    
    fin=open("E:\\CS177\\writeinmylab8.txt","r")
    print(fin.read())
    fin.close()
    
def lorem4(fileofkeysandvalues):
#Takes the file of key value pairs (which are separated by a space), reads in
#the file, and creates a dictionary out of the keys and values:
    
    ox={}
    for line in open(fileofkeysandvalues,'r'):
        key, value=str.split(line)
        ox[key]=value
    return(ox)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def lorem5(filehandle):
#Builds a dictionary of word counts and keeps track of what lines the
#words occur on:
    
#Opens the file twice:
    fin=open(filehandle,"r")
    fin2=open(filehandle,"r")
    cnt=0
    l=[]
    line=str(fin.read())
    for ch in '.,!?':
        line=str.replace(line,ch,' ')
    L=line.split()
    dic={}
    for wd in L:
        dic[wd]=dic.get(wd,0)+1
    print(dic,'\n')
    #so at this point you have each word with number of times in appears totaled
   
    for line in fin2.readlines():
#Runs through the lines in the file one at a time
        cnt=cnt+1
        for ch in '.,!?':
            line=str.replace(line,ch,' ')
        L=list(line.split())
        for wd in L:
#For each word in the line, does the following functions:
            test=dic.get(wd)
            tstlen=len(str(test))
#If the length of the value of the dictionary is greater than one,
            if tstlen > 1:
#that means the word has already been found so checks what last line was
                tsthld=int(test[tstlen-1:])
#If the line that the word is on is not the same as the value of the dictionary,
#the value is now the word count plus the current line
                if tsthld is not cnt:
                    dic[wd] = str(test) + "-" + str(cnt)
            else:
                dic[wd] = str(test) + "-" + str(cnt)

#For each key in the dictionary, prints the word, the word count, and the
#line/lines that the word is on:
    for key in dic:
        st1="Key word: "+key
        st2="   Word Count:"+ str(dic[key])[0]
        st3="   Line/Lines:"+ str(dic[key])[2:]
        print (st1,st2,st3)
#Closes the files
    fin.close()
    fin2.close()
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  


def lorem6(stringwithspaces):
#Takes a string and if it has whitespace at the beginning or end,
#removes the whitespace and returns a string with just the word/words:

#Strips the string of beginning and ending whitespace:
    y=stringwithspaces.strip()
#Returns the stripped string:
    return(y)

def ofinterest(number):
    y=number**2 + number + 23
    return(y)
#Total time: about 20 hours or more

