from visual import *
AU=1.5e11 #m
G=6.7e-11 #N*m^2/kg^2
speed=2*pi*AU/31536000.0 #m/s
dt=1000 #s
vscale=10000
trail=curve(color=color.green)
sun = sphere(pos=(0.,0.,0.), radius=vscale*695500., color=color.yellow)
sun.mass=1.98892e30 #kg
Earth = sphere(pos=(AU,0.,0.), radius=vscale*637800.1, color=color.blue)
Earth.mass=5.9742e24 #kg
Earth.velocity=vector(0,speed,0) #m/s
Earth.P=Earth.mass*Earth.velocity #kg m/s^2
Farrow=arrow(pos=Earth.pos, axis=sun.pos-Earth.pos, color=color.red)
Parrow=arrow(pos=Earth.pos, axis=Earth.velocity, color=color.orange)

while(1):
    rse=Earth.pos-sun.pos
    Force=-G*sun.mass*Earth.mass*rse/mag(rse)**3
    Earth.P=Earth.P+Force*dt
    Earth.pos=Earth.pos+Earth.P/Earth.mass*dt
    trail.append(pos=Earth.pos)
    Farrow.pos=Earth.pos
    Parrow.pos=Earth.pos
    Farrow.axis=Force/1.e12
    Parrow.axis=Earth.P/1.e18/4.25
