def fahr2cels(fahrenheit):
    print("Converts Degrees Fahrenheit to Degrees Celsius")
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius
    
def cels2fahr(celsius):
    print("Converts Degrees Celcius to Degrees Fahrenheit")
    fahrenheit = (9/5)* celsius + 32
    return fahrenheit

def cm2inch(cm):
    print("Converts centimeters to inches")
    inch = cm / 2.54
    return inch

def inch2cm(inch):
    print("Converts inches to centimeters")
    cm = 2.54 * inch
    return cm

def mi2km(mi):
    print("Converts miles to kilometers")
    km = mi * 1.609
    return km

def km2mi(km):
    print("Converts kilometers to miles")
    mi = km / 1.609
    return mi

def gal2L(gal):
    print("Converts gallons to liters")
    L = gal * 3.785
    return L

def L2gal(L):
    print("Converts liters to gallons")
    gal = L / 3.785
    return gal

def gal2imp(gal):
    print("gallons to imperial gallons")
    imp = 0.8327 * gal
    return imp

def imp2gal(imp):
    print("imperial gallons to US gallons")
    US = 1.20095 * imp
    return US

def lb2kg(lb):
    print("pounds to kilograms")
    kg = 2.2406 / lb
    return kg

def kg2lb(kg):
    print("kilograms to pounds")
    lb = 2.2406 * kg
    return lb

def kgm2(lbin2):
    print("Note: kgm2 = kilograms per (meter *meter)")
    print("Note: lbin2 = pounds per (inches * inches)")
    print("kilograms per (meter * meter) to pounds per (inches * inches)")
    kgm2 = 0.00142233433 / lbin2
    return kgm2

def mpg2kmpL(mpg):
    print("Converts miles per gallon to kilometers per liter")
    kmpL = mpg / 2.3521458
    return kmpL

def kmpL2mpg(kmpL):
    print("Converts kilometers per liter to miles per gallon")
    mpg = kmpL * 2.3521458
    return mpg

def Lpkm2mpg(Lp100km):
    print("Converts liters per 100 kilometers to miles per gallon")
    mpg = Lp100km / 235.21458
    return mpg

def mph(furlongsperfortnight):
    print("Converts furlongs per fortnight to miles per hour")
    mph = (furlongsperfortnight) / 2688
    return mph

def furperfort(mph):
    print("Converts miles per hour to furlongs per fortnight")
    furperfort = mph * 2688
    return furperfort

def par2mi(parsec):
    print("Converts parsecs to miles")
    mi = parsec * 1.91735281e13
    return mi
