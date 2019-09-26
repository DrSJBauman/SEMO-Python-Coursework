from visual import *
ball=sphere(pos=(-5,0,0), radius=0.5,color=color.cyan)
wallR=box(pos=(6,0,0),size=(0.2,12,12),color=color.green)
wallL=box(pos=(-6,0,0),size=(0.2,12,12),color=color.green)
wallT=box(pos=(0,6,0),size=(12,0.2,12),color=color.orange)
wallBo=box(pos=(0,-6,0),size=(12,0.2,12),color=color.orange)
wallBa=box(pos=(0,0,-6),size=(12,12,0.2),color=color.orange)
wallF=box(pos=(0,0,6),size=(12,12,0.2), color=color.orange, opacity=0)
ball.velocity=vector(25,5,15)
vscale=0.1
varr=arrow(pos=ball.pos,axis=vscale*ball.velocity, color=color.yellow)
ball.trail=curve(color=ball.color)
deltat=0.005
t=0
scene.autoscale=0
while t < 3:
    if ball.pos.x+0.5>wallR.pos.x-0.2:
        ball.velocity.x=-ball.velocity.x
    if ball.pos.x-0.5<wallL.pos.x+0.2:
        ball.velocity.x=-ball.velocity.x
    if ball.pos.z-0.5<wallBa.pos.z+0.2:
        ball.velocity.z=-ball.velocity.z
    if ball.pos.z+0.2>wallF.pos.z-0.2:
        ball.velocity.z=-ball.velocity.z
    if ball.pos.y+0.5>wallT.pos.y-0.2:
        ball.velocity.y=-ball.velocity.y
    if ball.pos.y-0.5<wallBo.pos.y+0.2:
        ball.velocity.y=-ball.velocity.y
    ball.pos=ball.pos+ball.velocity*deltat
    ball.trail.append(pos=ball.pos)
    varr.pos=ball.pos+ball.velocity*deltat
    varr.axis=vscale*ball.velocity
    t=t + deltat
    rate(100)
