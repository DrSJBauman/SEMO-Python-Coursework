def flips(n):
    import random
    #print("heads = 1, tails = 2")
    y=0
    h=1
    t=2
    for n in range(0,(n+1)):
        f=random.randint(1,2)
        #print(f)
        if f is h:
            y = y + 1
    print("Number of heads: ",y)

def roll(n):
    import random
    dice=0
    y=0
    for n in range(0,n):
        n1=random.randint(1,6)
        n2=random.randint(1,6)
        #print(dice)
        if (n1 + n2) is 7:
            y = y + 1
        dice = dice + (n1 + n2)
    print ("Number of sevens: ",y)

def firstheads():
    h,t=1,2
    import random
    i=1
    for i in range(1, 100):
        f=random.randint(1,2)
        if f is h:
            return i

def flipsnfirstheads(p):
    h,t=1,2
    import random
    import fu
    n=input("Enter a number of flips: ")
    n=int(n)
    y=0
    h=1
    t=2
    for i in range(1,(n+1)):
        f=random.randint(1,2)
        #print(f)
        if f is h:
            y = y + 1
            if y is 1:
                print ("Number of flips to return heads: ",i)
    print("Number of heads: ",y)

def geo(p):
    h,t=1,2
    import random
    n=input("Enter a number of flips: ")
    n=int(n)
    p=float(p)
    cnt=0
    cp=float(0)
    while cp != p:
        y=0
        for i in range(1,(n+1)):
            f=random.randint(1,2)
            #print(f)
            if f is h:
                y = y + 1
                if y is 1:
                    print ("Number of flips to return heads: ",i)
        print("Number of heads: ",y)
        cp=y/n
        cnt=cnt+1
        print (cp)
        print(p)
        input("Hit enter")
    print("Number of loops to get to p probability: ", cnt)

def geo2():
    h,t=1,2
    import random
    i=0
    f=0
    while f !=1:
        f=random.randint(1,2)
        print(f)
        input("Hit enter")
        i=i+1
    prob=1/(int(i))
    print("probability: ",prob)
    print("Number of flips to get first heads: ",i)
