def fact():
    n = int(eval(input("Enter a nonnegative integer:  ")))
    r = 1
    for i in range (1, n + 1):
        r = r * i
    print ("The factorial of ", n, " is ", r)
