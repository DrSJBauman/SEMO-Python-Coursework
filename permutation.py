def P(n,r):
    ret = 1
    for i in range(0, r):
        ret = ret * (n-i)
    return ret

