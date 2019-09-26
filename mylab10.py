def traits(stringname):
#Assigns a value(1-26) to each letter of the alphabet and adds up the value of
#one's name
    n=0
    stringname2=stringname.lower()
    ox={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    for k in stringname2:
        n=n+int(ox[k])
    print("Your name, ",stringname,", has a numeric value of:",n)

def traits2(stringname):
#Does the same as the above function, but can do full names
    n=0
    stringname2=stringname.lower()
    ox={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    for k in stringname2:
        y=ox.get(k,0)
        n=n+int(y)
    print("Your name, ",stringname,", has a numeric value of:",n)

def caesar8encode(strng,shift):
#A coding function that shifts lowercase letters over by their ASCII values to
#encode a message
    s=""
    for i in strng:
        n=ord(i)
#Make caesar cypher the value of shift
        n=n+shift
        c=chr(n)
        s=s+c
    print(s)

def caesar8decode(strng,shift):
#Decodes the above function's result if the same shift is used
    s=""
    for i in strng:
        n=ord(i)
#Make caesar cypher the value of shift
        n=n-shift
        c=chr(n)
        s=s+c
    print(s)


def caesar9encode(strng,shift):
#A caesar shift that does not fail when  the ASCII values go out of the range of
#the lowercase letters
    s=""
    if 0>shift or shift>25:
        return("Caesar cypher key must be from one to 25!!!! Stooge!")
    for i in strng:
        n=ord(i)
#Make caesar cypher the value of shift
        n=n+shift
#If the ASCII values become greater than that of z, they wrap around back to the
#beginning of the alphabet (ASCII value 97)
        if n >122:
            n=n-122+96
        c=chr(n)
        s=s+c
    print(s)

def caesar9decode(strng,shift):
#The decoding function for the above function
    s=""
    if 1>shift or shift>25:
        return("Caesar cypher key must be from one to 25!!!! Stooge!")
    for i in strng:
        n=ord(i)
#Make caesar cypher the value of shift
        n=n-shift
#If the ASCII values become less than that of a, they wrap around back to the
#end of the alphabet (ASCII value 122)
        if n <97:
            n=n+123-97
        c=chr(n)
        s=s+c
    print(s)

def eligible():
#Determines whether one is eligible to be a US representative or senator, given
#their age and how many years they have been a US citizen
    n1=input("Enter your age: ")
    n2=input("How many years have you been a US citizen? ")
    print('\n')
    if int(n1) >= 25 and int(n2) >=7:
            print("You are eligible to be a US representative.")
    else: print("You are not eligible to be a US representative.")
    if int(n1) >= 30 and int(n2) >= 9:
            print("You are eligible to be a US senator.")
    else: print("You are not eligible to be a US senator.")

def easter(year):
#Calculates the date of easter, given the year
#The calculations for numbers d and e (the date is March 22 + d + e)
    a=year%19
    b=year%4
    c=year%7
    d=((19*a) +24)%30
    e=((2*b)+(4*c)+(6*d)+5)%7
    t=d+e
    m=3
#Makes the month april if the days go past march 31
    if t >9:
        m=4
        if t<30:
            t=30-t
        else: t=t-30+22
    else: t=t+22
#Checks if the year is in the working range for the function
    if year >=1982 and year <=2048:
        print("Easter's date is: ",m,"/",t," for the year,",year)
    else:print("Year is not in proper range (1982-2048)")
        
def easter2(year):
#Calculates the date of easter, given the year
#The calculations for numbers d and e (the date is March 22 + d + e)
    a=year%19
    b=year%4
    c=year%7
    d=((19*a) +24)%30
    e=((2*b)+(4*c)+(6*d)+5)%7
    t=d+e
    m=3
#Makes the month april if the days go past march 31
    if t >9:
        m=4
        if t<30:
            t=30-t
        else: t=t-30+22
    else: t=t+22
#Checks the dates that work or that have to be worked with
    if year>=1900 and year<=2099 and year!=1954 and year!=1981 and year!=2049 and year!=2076:
        print("Easter's date is: ",m,"/",t," for the year,",year)
#For these dates, one week must be subtracted
    elif year == 1954 or year==1981 or year==2049 or year==2076:
        t=t-7
        if t<1:
            m=3
        print("Easter's date is: ",m,"/",t," for the year,",year)

def leapYear(year):
#Calculates whether or not a year is a leap year
    r=False
    if year%4==0:
        r=True
        if year%100==0:
            if year%400==0:
                r=True
            else: r=False
#Returns True if year is a leap year and False if not
    return r

def daynumber(month,day,year):
#Returns the day of the year, given a date
    dayNum=(31*(month-1))+day
#If the month is later than February, does a calculation
    if month >2:
        dayNum=dayNum-((4*month +23)//10)
#If it is a leapyear and after February 29, adds a day
    if leapYear(year) == True:
        if month>2:
            dayNum=dayNum+1
    return dayNum

def Fibonacci(number):
#Adds the number to itself, then adds the last two numbers together and keeps
#going until the nth number.(performs a Fibonacci sequence to the nth Fibonacci number)

#Establishes 1 as the first two numbers so that the sequence can start somewhere
    L=[1,1]
    f=0
#While the length of the list  is less than n, the sequence continues, adding
#the new values to the list
    while len(L)<number:
        f=L[-1]+L[-2]
        L.append(f)
    return(L[-1])
    
def Syracuse(n):
#Divides even numbers by two and multiplies odd numbers by 3 and adds one, until
#the number becomes one. Prints the sequence of numbers until one is achieved
    print(n)
    while n != 1:
        if n/2 == int(n/2):
            n=n/2
            print(n)
        else:
            n=(3*n)+1
            print(n)

def GCD(m,n):
#Finds the GCD of two given numbers
    m=m
    n=n
    while m!=0:
        n,m=m,n%m
    print(n,'is the GCD of the original m and n')


def degreedays(ListOfAvgDailyTemps):
#Calculates the number of heating degree days and cooling degree days
#given a list of average daily temperatures.    
    cdd=0
    hdd=0
    for i in ListOfAvgDailyTemps:
#If the temp is under 60, adds one heating degree day
        if i <60:
            hdd=hdd+(60-i)
        if i >80:
#If the temp is above 80, adds one cooling degree day
            cdd=cdd+(i-80)
    print("cooling degree days:",cdd)
    print("heating degree days:",hdd)

def randomwalk(steps):
#A random walk is when, for example, someone stands on a straight
#sidewalk and flips a coin.  If it is heads, they take a step
#forward, and if tails, a step backwards.  For a given number of
#steps, returns the number of steps that they are either forward or
#backward from the starting point(total displacement)
    import random
    y=0
    x=0
    z=0
    for i in range(0,(steps+1)):
        f=random.choice([-1,1])
        if f is -1:
            x=x-1
        if f is 1:
            y = y + 1
    z=x+y
    if z >0:
        print("Will end up ",z,"step(s) forward from starting point")
    if z<0:
        print("Will end up",-z,"step(s) backward from starting point")
