#Stephen Bauman  PH230  1-20-10
from visual import *
baseball=sphere(pos=vector(-4,-2,5), radius=0.20, color=color.white)
tennisball=sphere(pos=vector(3,1,-2), radius=0.15, color=color.green)
bt=arrow(pos=baseball.pos, axis=tennisball.pos-baseball.pos, color=color.red)
#arrow(pos=vector(0,0,0), axis=vector(6,6,0), color=color.white)
#arrow(pos=vector(2,1,3), axis=vector(3,-4,0), color=color.cyan)
#arrow(pos=vector(2,4,0), axis=vector(-5,-5,0), color=color.orange)
print tennisball.pos

t=0
while t<10:
    t=t+0.5
    print(t)
print("End of program")
