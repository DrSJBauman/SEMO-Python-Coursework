from visual import *
from visual.graph import *
AU=1.5e11 #m 
G=6.7e-11 #N*m^2/kg^2
speed=2.5*pi*AU/31536000.0 #m/s
dt=10000 #s
time=0 #s
vscale=10000 #Makes the numbers work better
trail=curve(color=color.green)

sun = sphere(pos=(0.,0.,0.), radius=vscale*695500., color=color.yellow)
sun.mass=1.98892e30 #kg

Earth = sphere(pos=(AU,0.,0.), radius=vscale*637800.1, color=color.blue)
Earth.mass=5.9742e24 #kg
Earth.velocity=vector(0,speed,0) #m/s
Earth.P=Earth.mass*Earth.velocity #kg m/s^2

Farrow=arrow(pos=Earth.pos, axis=sun.pos-Earth.pos, color=color.red)
Parrow=arrow(pos=Earth.pos, axis=Earth.velocity, color=color.orange)

A=vector(-2*AU,0,0) #Sets up positions for the arrows
B=vector(2*AU,0,0)
S=sun.pos

LAarrow=arrow(pos=A, axis=(0,0,0), color=color.cyan) 
LBarrow=arrow(pos=B, axis=(0,0,0), color=color.orange)
LSarrow=arrow(pos=S, axis=(0,0,0), color=color.yellow)

graph=gcurve(color=color.cyan)
graph2=gcurve(color=color.orange)
graph3=gcurve(color=color.yellow)

while(1):
    rse=Earth.pos-sun.pos #m Distance between Earth and Sun
    Force=-G*sun.mass*Earth.mass*rse/mag(rse)**3 #N Updates gravitational force
    Earth.P=Earth.P+Force*dt #kg m/s Updates momentum
    Earth.pos=Earth.pos+Earth.P/Earth.mass*dt #m Updates position

    trail.append(pos=Earth.pos)
    Farrow.pos=Earth.pos
    Parrow.pos=Earth.pos
    Farrow.axis=Force/1.e12
    Parrow.axis=Earth.P/1.e18/4.25

    LA=cross((Earth.pos-A),Earth.P) # Calculates Angular momentums
    LB=cross((Earth.pos-B),Earth.P) # at the various positions
    LS=cross((Earth.pos-S),Earth.P)

    LAarrow.axis=LA*5e-30 #Makes the arrows show the Angular momentums
    LBarrow.axis=LB*5e-30 #at their designated points
    LSarrow.axis=LS*5e-30

    time=time+dt
    graph.plot(pos=(time, mag(LA)))
    graph2.plot(pos=(time, mag(LB)))
    graph3.plot(pos=(time, mag(LS)))
