#Stephen Bauman
#PH230-Pendulum
#2-25-10

from visual import *
from visual.graph import *
floor=box(pos=(0,2,0),size=(20,1,20),color=color.green)
rod=cylinder(pos=(-9,25,0),axis=(18,0,0),radius=.3, color=color.cyan)
scene.center=(0,rod.pos.y,0)
scene.autoscale=0

f1=frame() #Set up frames to rotate the strings and plumbs
f2=frame()

string1=cylinder(frame=f1,pos=(-5,25,0),axis=(0,-20,0),radius=.2,color=color.orange)
plumb1=sphere(frame=f1,pos=(-5,5,0),radius=1.5,color=color.orange)
graph1=gcurve(color=color.orange)

string2=cylinder(frame=f2,pos=(5,25,0),axis=(0,-20,0),radius=.2,color=color.yellow)
plumb2=sphere(frame=f2,pos=(5,5,0),radius=1.5,color=color.yellow)
graph2=gcurve(color=color.yellow)

theta0=178. #initial angle in degrees

theta1=theta0*pi/180 #converts to radians
theta1dot=0.

theta2=theta0*pi/180
theta2dot=0.

dt=0.001 #time step
t=0 #s
L=.5
g=9.8 #m/s**2
omega=sqrt(g/L)

f1.rotate(angle=theta1,origin=(0,25,0)) #Gives the strings their initial angles
f2.rotate(angle=theta1,origin=(0,25,0))

while(1):
    rate(1500)
    theta1dotdot=-omega**2*sin(theta1) #do first pendulum(small angle way)
    theta1dot=theta1dot+theta1dotdot*dt #finds 1st derivative of theta1
    theta1=theta1+theta1dot*dt #finds theta1 again to plug in on the next loop
    f1.rotate(angle=theta1dot*dt,origin=(0,25,0)) #rotates to the new angle

    theta2dotdot=-omega**2*(theta2) #do second pendulum(not true way)
    theta2dot=theta2dot+theta2dotdot*dt
    theta2=theta2+theta2dot*dt
    f2.rotate(angle=theta2dot*dt,origin=(0,25,0))

    t=t+dt
    graph1.plot(pos=(t,L*theta1))#Graphs the angle vs time
    graph2.plot(pos=(t,L*theta2))
