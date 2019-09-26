def test():
    #Counts the number of words in the bmi file.
    #But what counts as words?
    import os
    os.getcwd()
    fin=open("bmi2.py","r")
    L=str(fin.readlines())
    cnt=(L.count("def"))+(L.count("BMI"))+(L.count("height"))+(L.count("weight"))+(L.count("import"))+(L.count("math"))+(L.count("return"))+(L.count("sqrt"))
    fin.close()
    return cnt
