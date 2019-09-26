import math
def triangleArea(a, b, c):
    s=(a+b+c)/2
    print("Length of s: ",s)
    A=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of triangle:")
    return A

def leapYear(year):
    r=False
    if year%4==0:
        r=True
        if year%100==0:
            if year%400==0:
                r=True
            else: r=False
    return r
