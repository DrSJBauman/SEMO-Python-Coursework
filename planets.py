#Stephen Bauman  PH230  1-20-10
from visual import *
sun=sphere(pos=vector(0,0,0),radius=7.0e9,color=color.yellow)
mercury=sphere(pos=vector(5.8e10,0,0),radius=2.4e9,color=color.orange)
venus=sphere(pos=vector(-1.1e11,0,0),radius=6.0e9,color=color.magenta)
earth=sphere(pos=vector(0,1.5e11,0),radius=6.4e9,color=color.blue)
a1=arrow(pos=(earth.pos),axis=(mercury.pos-earth.pos),color=color.cyan)
a2=arrow(pos=(earth.pos),axis=(0.5*(venus.pos-earth.pos)),color=color.white)
#color.gray DOES NOT work!

step=0
deltar=vector(1e9,1e9,0)
while step<100:
    step=step+1
    print step
    mercury.pos=mercury.pos+deltar
    rate(20)
    a1.axis=mercury.pos-earth.pos
print "End of program, step=",step


#Returns numbers 1 through 100 and "End of program, step=100"
