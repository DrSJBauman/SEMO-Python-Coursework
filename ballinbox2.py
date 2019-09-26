from visual import *
#Makes colors so red/cyan glasses could see the scene: scene.stereo='redcyan'
#Creates a ball, given a position of the center, a radius, and a color:
ball=sphere(pos=(-5,0,0), radius=0.5,color=color.cyan)
#Creates walls out of thin boxes given a position of the center, sizes in x y and z directions, and a color:
wallR=box(pos=(6,0,0),size=(0.2,12,12),color=color.green)
wallL=box(pos=(-6,0,0),size=(0.2,12,12),color=color.green)
wallT=box(pos=(0,6,0),size=(12,0.2,12),color=color.orange)
wallBo=box(pos=(0,-6,0),size=(12,0.2,12),color=color.orange)
wallBa=box(pos=(0,0,-6),size=(12,12,0.2),color=color.orange)
wallF=box(pos=(0,0,6),size=(12,12,0.2), color=color.orange, opacity=0)
#Gives the ball a velocity with a vector for the direction:
ball.velocity=vector(25,5,15)
#Gives a scale to shrink down the arrow below
vscale=0.1
#Creates an arrow with tail on the center of the ball and nose of 0.1 * the velocity coordinates of the ball:
varr=arrow(pos=ball.pos,axis=vscale*ball.velocity, color=color.yellow)
#Causes the ball to leave a trail:
ball.trail=curve(color=ball.color)
#Used to keep track of time so that the ball can appear to move:
deltat=0.005
t=0
#Keeps the camera stationary:
scene.autoscale=0
#Makes the ball keep bouncing 'forever':
while 1:
    #Causes the ball to change velocity in the opposite direction
    #if they 'strike' a wall:
    if ball.pos.x+0.5>wallR.pos.x-0.2:
        ball.velocity.x=-ball.velocity.x
        ball.color=color.blue
    if ball.pos.x-0.5<wallL.pos.x+0.2:
        ball.velocity.x=-ball.velocity.x
        ball.color=color.red
    if ball.pos.z-0.5<wallBa.pos.z+0.2:
        ball.velocity.z=-ball.velocity.z
        ball.color=color.green
    if ball.pos.z+0.2>wallF.pos.z-0.2:
        ball.velocity.z=-ball.velocity.z
        ball.color=color.magenta
    if ball.pos.y+0.5>wallT.pos.y-0.2:
        ball.velocity.y=-ball.velocity.y
        ball.color=color.yellow
    if ball.pos.y-0.5<wallBo.pos.y+0.2:
        ball.velocity.y=-ball.velocity.y
        ball.color=color.black
    #Makes the ball move by intervals of the velocity * delta t
    ball.pos=ball.pos+ball.velocity*deltat
    #Makes the ball leave a dot every interval of delta t
    ball.trail.append(pos=ball.pos)
    #Makes the arrow stay on the ball and point where it is going
    varr.pos=ball.pos+ball.velocity*deltat
    #Keeps the arrow the right size
    varr.axis=vscale*ball.velocity
    #Adds 0.005 to t, making it as though time is being counted up by 0.005
    t=t + deltat
    #Slows down the speed of the program
    rate(100)
