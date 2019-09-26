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

def lorem56():
#Builds a dictionary of word counts and keeps track of what lines the
#words occur on:
    
#Opens the file twice:
    fin=open("E:\\CS177\\MOSESHULK.txt","r")
    fin2=open("E:\\CS177\\MOSESHULK.txt","r")
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
  
    ox={}
    for line in fin2.readlines():
        cnt=cnt+1
        for ch in '.,!?':
            line=str.replace(line,ch,' ')
        L=list(line.split())
        for wd in L:
            #Makes the line number the value of the dictionary:
            ox[wd]=cnt
        Li=list(wd)
        Li2=list(str(cnt))
            
#Problem:Only returns the most recent line that the word appears on
            #If the word is already in the dictionary, is makes the
            #line number the new value of the dictionary:
        for wd in L:   
            ox[wd]=ox.get(wd,cnt)
        Li3=list(str(cnt))
        #print(L)
        #n=input('Press enter')    
    print(ox)
    fin.close()
    fin2.close()
  

def lorem567():
    fin=open("E:\\CS177\\MOSESHULK.txt","r")
    fin2=open("E:\\CS177\\MOSESHULK.txt","r")
    cnt=0
    li=[]
    ox={}
    for line in fin2.readlines():
        cnt=cnt+1
        li=[str(cnt)]
        for ch in '.,!?':
            line=str.replace(line,ch,' ')
        L=list(line.split())
        for wd in L:
            #Makes the line number the value of the dictionary:
            if ox.keys():
                ox[wd]=ox[wd]+1
            else: ox[wd]=1
            #ox[wd]=ox.get(wd,li.append(cnt))
            #if wd in ox is True:
                #if cnt > ox[wd]:
                
           
    print(ox)
    fin.close()
    fin2.close()

def lorem5():
    fin=open("E:\\CS177\\MOSESHULK.txt","r")
    fin2=open("E:\\CS177\\MOSESHULK.txt","r")
    cnt=0
    li=[]
    ox1={}
    ox2={}
    ox3={}
    ox4={}
    ox5={}
    for line in fin2.readlines():
        cnt=cnt+1
        li=[str(cnt)]
        for ch in '.,!?':
            line=str.replace(line,ch,' ')
        L=list(line.split())
        for wd in L:
            if cnt is 1:
                ox1[wd]=cnt
            elif cnt is 2:
                ox2[wd]=cnt
            elif cnt is 3:
                ox3[wd]=cnt
            elif cnt is 4:
                ox4[wd]=cnt
            elif cnt is 5:
                ox5[wd]=cnt
    print(ox1,ox2,ox3,ox4,ox5)
        
    fin.close()
    fin2.close()
  

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





# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def lorem56dad():
#Builds a dictionary of word counts and keeps track of what lines the
#words occur on:
    
#Opens the file twice:
    fin=open("E:\\CS177\\MOSESHULK.txt","r")
    fin2=open("E:\\CS177\\MOSESHULK.txt","r")
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
    #so at this point you have each word with number of times totaled

    # !@!@ try to add a number to the value field
    #dic['the']
    #sorted(dic.keys())
    #test=dic.get('the')
    #print (test)
    #test = str(test) + "-3-4"
    #print (test)
    #dic['the'] = test
    #print (dic)
    #you can piece text together in a key value so can you take your
    #dic dictionary and below loop thru the lines words and
    #add to the value the line number.....
    #!!! will need to scan thru the value to see if that line has already
    #been added to the keys value
    # ex the word 'the' will be 3 and then '3-3' and then when found again
    #on line 3 it can check length of field, if >1 then it has found it
    # lets try something....
      
      
    ox={}
    for line in fin2.readlines():
        cnt=cnt+1
        for ch in '.,!?':
            line=str.replace(line,ch,' ')
        L=list(line.split())
        for wd in L:
            test=dic.get(wd)
            #print(test)
            tstlen=len(str(test))
            #print (tstlen)
            if tstlen > 1:
                #has already been found so check what last row was
                tsthld=int(test[tstlen-1:])
                #print (tsthld)
                #print (cnt)
                if tsthld is not cnt:
                    dic[wd] = str(test) + "-" + str(cnt)
            else:
                dic[wd] = str(test) + "-" + str(cnt)

    for key in dic:
        #st=str("("+key+", "+str(dic[key])+")"+"\n")
        st1="Key word: "+key
        st2="   Word Count:"+ str(dic[key])[0]
        st3="   Line/Lines:"+ str(dic[key])[2:]
        print (st1,st2,st3)

    
        #    ox[wd]=cnt
        #print (ox)
            
        #Li=list(wd)
        #Li2=list(str(cnt))
            
#Problem:Only returns the most recent line that the word appears on
            #If the word is already in the dictionary, is makes the
            #line number the new value of the dictionary:
        #for wd in L:   
        #    ox[wd]=ox.get(wd,cnt)
        #Li3=list(str(cnt))
        #print(L)
        #n=input('Press enter')    
    #print(ox)
    fin.close()
    fin2.close()
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
