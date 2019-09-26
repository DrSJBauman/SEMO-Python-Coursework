#Stephen Bauman
#2-18-10
#Spring Friction

from visual import *
from visual.graph import *
Floor=box(pos=(6,-1.5,0), size=(12,.25,4),color=color.green)
Wall=box(pos=(0,0,0),size=(.25,3,4),color=color.green)
Block=box(pos=(6,0,0),size=(3,3,3),color=color.orange)
Spring=helix(pos=Wall.pos,axis=vector(Block.pos.x,0,0),radius=1.5,color=color.cyan)
Block.mass=10. #kg Mass of Block
Block.velocity=vector(.75,0,0) #m/s Velocity of the block
Block.P=Block.mass*Block.velocity #kg m/s  Momentum of the block
Lo=(6,0,0) #Equilibrium position
dt=.005 #Change in time

graph=gcurve(color=color.yellow) #Creates a graph
graph2=gcurve(color=color.green)
graph3=gcurve(color=color.red)
graph4=gcurve(color=color.cyan)
time=0 #sec  Time for the x-axis of the graph

k=0.5 #N/m Spring constant
mu=0.1 #Coefficient of friction
N=1  #Power of the velocity

while(1):
    rate=10
    r=Block.pos-Lo # Change in x
    F=-k*r #N  Force of the spring on the Block
    Ff=-mu*(mag(Block.velocity)**N)*norm(Block.velocity)#N Friction Force
    Fnet=F+Ff #Net Force
    Block.P=Block.P+Fnet*dt #Changes the Block's momentum using the force
    Block.pos=Block.pos+Block.P/Block.mass*dt #Changes the Block's position using the momentum
    Block.velocity=Block.P/Block.mass
    KEf=.5*Block.mass*(Block.velocity.x)**2 #Update KE of the spring

    Spring.Energy=.5*k*(r.x)**2  #Spring Potential Energy
    Spring.axis=vector(Block.pos.x,0,0) #Makes the Spring stay on the Block

    time=time+dt #Counts time in seconds for the graph
    graph.plot(pos=(time,Block.velocity.x)) #Plots the graph with velocity vs time
    graph2.plot(pos=(time,KEf)) #Plots KE vs time
    graph3.plot(pos=(time,Spring.Energy)) #Plots spring energy vs time
    graph4.plot(pos=(time, Spring.Energy+KEf)) #Plots total energy vs time
