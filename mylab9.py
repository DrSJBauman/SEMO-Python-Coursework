import pickle
import os
os.getcwd()
s="E:\\CS177"
os.chdir(s)
def test():
    L=[1,2,3,4,5]
#Opens the file for binary writing:
    fout=open('first.pickle','wb')
#Dumps the list L into the file:
    pickle.dump(L,fout)
    fout.close()
#Opens the binary file for reading:
    fin=open("first.pickle",'rb')
#Loads the file again:
    M=pickle.load(fin)
    print(M)
    fin.close()
    
def test2():
#Opens and closes the file and assigns it to f:
    with open ('first.pickle','rb') as f:
#Assigns the file, f, to the variable, data:
        data=pickle.load(f)
    print(data)

def pickdump():
    fin=open("LOREM.txt","r")
#Reads in a file line by line:
    line=str(fin.read())
    #for ch in '.,?!':
        
#Breaks each line into words:
    L=line.split()
    ox={}
    for wd in L:
#Builds a dictionary of word counts:
        ox[wd]=ox.get(wd,0)+1
    fin.close()
    fout=open('wordcounts.pickle','wb')
    pickle.dump(ox,fout)
    fout.close()

def pickload():
#Unpickles the file wordcounts.pickle and prints the fist 10
#and last 10 words and counts
    j=open('wordcounts.pickle','rb')
    k=open('wordcounts.pickle','rb')
#Loads the dictionary in the file into a list, L and a dictionary, H:
    G=(pickle.load(j))
    L=list()
    H=dict(pickle.load(k))
    L=L+list(G)
#Takes the first and last ten words in the list L:
    r=L[:10]+L[-10:]
#Runs through those twenty words and gets the values associated with them
#in the dictionary, H
    for wd in r:
        v=H.get(wd)
        print("Word:  "+wd+"   Word Count:"+str(v))
    j.close()

def wordclean():
#Removes whitespace and punctuation from the file and makes each word lowercase
#Then counts the words in a dictionary and pickles it to wordcounts.pickle:
    fin=open("E:\\CS177\\LOREM.txt","r")
    line=str(fin.read())
#Replaces the punctuation with spaces:
    for ch in '!@#$%^&*(),.?/;:"[]{}':
        line=str.replace(line,ch,' ')
#Splits the file into words and makes them lowercase:
    L=line.lower()
    L=list(line.split())
    ox={}
#Makes a dictionary of word counts:
    for wd in L:
        ox[wd]=ox.get(wd,0)+1
#Dumps the dictionary to the file and closes the files:
    fout=open('wordcounts.pickle','wb')
    pickle.dump(ox,fout)
    fin.close()
    fout.close()
           
