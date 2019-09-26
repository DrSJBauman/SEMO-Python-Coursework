import random
def bernoulli(p):
    r=0
    if random.random()<=p: r=1
    return r

def binomial(n,p):
    suc=0
    for i in range(0,n):
        x = random.random() 
        if x<=p: r =1
        if x>p: r = 0
        if r == 1:
            suc=suc+1
    return suc

def geometric(p):
    for i in range(1,1000):
        x=random.random()
        if x<=p:r=1
        if x>p:r=0
        if r==1:
            return i
