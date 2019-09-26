def fact(n):
    #Returns the factorial of n
    r=1
    for i in range(1, n+1):
        r=i*r
    return r

def P(n,r):
    #Returns number of permutations of r distinct objects selected
    # from n distinct objects. Order matters.
    ret=1
    for i in range(0,r):
        ret=ret*(n-i)
    return ret

def C(n,r):
    #Returns the number of combinations of r objects selected
    # from n distinct objects
    ret=1
    if (r>0) and (r<n):
        ret=(fact(n)//(fact(r)*fact(n-r)))
    return ret

def digits(n):
    #Returns the number of decimal digits needed to write down the positive
    # integer n in the usual decimal notation
    count = 1
    while n >= 10:
        n = n // 10
        count = count + 1
    return count

def main():
    import mylab3
    import mylab2
    a=mylab3.C(25,5)
    b=mylab3.C(15,3)
    c=mylab2.binomial(8,3/5)
    d=mylab3.C(52,5)
    e=mylab3.digits(mylab3.P(50,34))
    f=mylab3.digits(mylab3.C(50,24))
    g=mylab3.digits(10000)
    print("1. ",a)
    print("2. ",b)
    print("3. ",c)
    print("4. ",d)
    print("5. ",e)
    print("6. ",f)
    print("7. ",g)
    
   
    
