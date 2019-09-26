def workdirectory():
    import os
    os.getcwd()
    s="E:\\CS177"
    os.chdir(s)
    os.getcwd()
    fin.close()

def printfile(filename):
    import os
    os.getcwd()
    s="E:\\CS177"
    os.chdir(s)
    fin=open(filename,"r")
    print(fin.read())
    fin.close()

def writefile():
    import os
    s="E:\\CS177"
    os.chdir(s)
    fout=open("why.py","w")
    fout.write("How much wood could a woodchuck chuck if a woodchuck could chuck wood?")
    fout.close()
