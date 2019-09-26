from visual import *
#Objects created
wheelfl=sphere(pos=(-490,-4,-4), radius=2,color=(.1,.1,.1))
wheelfr=sphere(pos=(-490,-4,4), radius=2,color=(.1,.1,.1))
wheelbr=sphere(pos=(-496,-4,4), radius=2,color=(.1,.1,.1))
wheelbl=sphere(pos=(-496,-4,-4), radius=2,color=(.1,.1,.1))
body=box(pos=(-490,0,0),size=(15,6,8),color=(.4,.0,.0))
nose=arrow(pos=(-500,0,0),axis=vector(25,0,0),color=color.yellow)
road=box(pos=(0,-6.1,-4),size=(2000,.1,20),color=(.2,.2,.2))
stripe=box(pos=(0,-6.1,-4),size=(2000,.11,.3),color=color.yellow)
#Velocities assigned
wheelfl.velocity=vector(400,0,0)
wheelfr.velocity=vector(400,0,0)
wheelbr.velocity=vector(400,0,0)
wheelbl.velocity=vector(400,0,0)
body.velocity=vector(400,0,0)
nose.velocity=vector(400,0,0)
deltat=0.005
t=0
while t<3:
    wheelfl.pos=wheelfl.pos+wheelfl.velocity*deltat
    wheelfr.pos=wheelfr.pos+wheelfr.velocity*deltat
    wheelbr.pos=wheelbr.pos+wheelbr.velocity*deltat
    wheelbl.pos=wheelbl.pos+wheelbl.velocity*deltat
    body.pos=body.pos+body.velocity*deltat
    nose.pos=nose.pos+nose.velocity*deltat
    t=t+deltat
    rate(100)
