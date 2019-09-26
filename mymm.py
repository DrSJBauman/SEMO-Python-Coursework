import math
import mylab4
import random
def sphereVol(radius):
    #Returns the volume of a sphere, given the radius
    V=(4/3)* math.pi * radius**3
    return V

def windChill(T,V):
    #Returns the wind chill index when given temperature and wind speed
    #T=input("Enter the temperature in degrees Fahrenheit")
    #V=input("Enter the wind speed in miles per hour")
    if T<=50:
        if V>3:        
            chill=35.74 + 0.6215*T - 35.75*(V**0.16) + 0.4275*T*(V**0.16)
        else: return T
    else:return T
    return chill

def dayOfYear(month,day,year):
    d=31*(month-1) + day
    if month>2:
        d=d - ((4*month + 23)//10)
        if mylab4.leapYear(year)==True:
            d=d + 1
    return d

def under(x,y):
    if (x**2)+(y**2)<=1:
        return 1
    if (x**2)+(y**2)>1:
        return 0

def times(n):
    cnt=0
    for i in range(n):
        x=random.random()
        y=random.random()
        if under(x,y)==1:
            cnt=cnt+1
    return cnt

def approxPi(n):
    return 4*((times(n))/n)

def approxPi2(n):
    sum=0
    for i in range(1,n):
        x = random.random()
        y = random.random()
        #print(x)
        #print(y)
        if x**2 + y**2<=1:
            sum=sum+1
    return(4*(sum/n)) 

def test1():
    print("Sphere Volume")
    #Tests sphereVol with given values
    print("The volumes of spheres with radii 1, 2, and square root of 2:")
    print(sphereVol(1) , sphereVol(2) , sphereVol(math.sqrt(2)))
    print()
    print("Wind Chill")
    #Tests windChill with given values
    print("Temperature=50, wind speed=13: Wind chill index=",windChill(50,13))
    print("Temperature=30, wind speed=30: Wind chill index=",windChill(30,30))
    print("Temperature=-10, wind speed=40: Wind chill index=",windChill(-10,40))
    print()
    print("Day of the year")
    #Tests dayOfYear with given values
    print("On October 23, 1960, the day of the year is:",dayOfYear(10,23,1960))
    print("On December 25, 2000, the day of the year is:",dayOfYear(12,25,2000))
    print("On February 15, 1904, the day of the year is:",dayOfYear(2,15,1904))
    print("On March 15, 1600, the day of the year is:",dayOfYear(3,15,1600))
    print()
    print("Approximations of the Value of Pi")
    #Tests approxPi and approxPi2 with given values
    print("approxPi(10)=",approxPi(10),"approxPi(100)=",approxPi(100))
    print("approxPi(1000)=",approxPi(1000),"approxPi(10000)=",approxPi(10000))
    print("approxPi2(10)=",approxPi2(10),"approxPi2(100)=",approxPi2(100))
    print("approxPi2(1000)=",approxPi2(1000),"approxPi2(10000)=",approxPi2(10000))
    print("Approximate values of Pi compared to the math function value of pi")
    print(approxPi(1000),",",approxPi(1000),",",approxPi(1000),",",approxPi(1000))
    print(approxPi(1000),",",approxPi(1000),",",approxPi(1000),",",approxPi(1000),",",approxPi(1000),",",approxPi(1000))
    print("Math function value of pi")
    print(math.pi)
