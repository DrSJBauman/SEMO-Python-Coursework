from visual import *
t=0
g=9.8 #m/s^2
speed=20 #m/s
dt=.01 #sec
Xo=vector(0.,0.,0.)
ball=sphere(pos=Xo, radius=1, color=color.blue)
ball.mass=1 #kg
Force=vector(0.,-ball.mass*g,0.)
trail=curve(color=color.red)
ground=box(pos=(25.,-.5,0.),length= 50., width=20.,height=.5, color=color.white)
scene.autoscale=0
for theta in range(5,95,10):
    theta=theta *pi/180. #convert to radians
    ball.velocity=vector(speed*cos(theta),speed*sin(theta),0.)
    ball.p=ball.mass*ball.velocity
    ball.pos=Xo
    while (ball.pos.y>=0):
        rate(100)
        ball.p=ball.p+Force*dt
        ball.pos=ball.pos+ball.p/ball.mass*dt
        trail.append(pos=ball.pos)
