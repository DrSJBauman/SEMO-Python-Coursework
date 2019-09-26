#Stephen Bauman
#2-18-10
#Spring Energy

from visual import *
from visual.graph import *
Floor=box(pos=(6,-1.5,0), size=(12,.25,4),color=color.green)
Wall=box(pos=(0,0,0),size=(.25,3,4),color=color.green)
Block=box(pos=(6,0,0),size=(3,3,3),color=color.orange)
Spring=helix(pos=Wall.pos,axis=vector(Block.pos.x,0,0),radius=1.5,color=color.cyan)
Block.mass=10. #kg Mass of Block
Block.velocity=vector(.75,0,0) #m/s Velocity of the block
Block.P=Block.mass*Block.velocity #kg m/s  Momentum of the block
k=0.5 #N/m spring constant
Lo=(6,0,0) #equilibrium position
dt=.005 #change in time

graph=gcurve(color=color.yellow) #creates a graph
graph2=gcurve(color=color.green)
graph3=gcurve(color=color.red)
graph4=gcurve(color=color.cyan)
time=0 #sec  time for the x-axis of the graph
#KEi=.5*Block.mass*(Block.velocity.x)**2 #J

while(1):
    rate=10
    r=Block.pos-Lo # change in x
    F=-k*r #N  force of the spring on the Block
    Block.P=Block.P+F*dt #changes the Block's momentum using the force
    Block.pos=Block.pos+Block.P/Block.mass*dt #changes the Block's position using the momentum
    Block.velocity=Block.P/Block.mass
    KEf=.5*Block.mass*(Block.velocity.x)**2 #update KE of the spring
    Spring.Energy=.5*k*(r.x)**2
    Spring.axis=vector(Block.pos.x,0,0) #Makes the Spring stay on the Block
    time=time+dt #counts time in seconds for the graph
    graph.plot(pos=(time,Block.pos.x)) #plots the graph with Block.pos vs time
    graph2.plot(pos=(time,KEf)) #plots KE vs time
    graph3.plot(pos=(time,Spring.Energy)) #plots spring energy vs time
    graph4.plot(pos=(time, Spring.Energy+KEf)) #plots total energy vs time
