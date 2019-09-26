def BMI(height, weight):
    return (weight * 703) / (height * height)

def height(BMI, weight):
    import math
    return (math.sqrt((weight * 703) / BMI))

def weight(height, BMI):
    return ((BMI * (height ** 2)) / 703)
