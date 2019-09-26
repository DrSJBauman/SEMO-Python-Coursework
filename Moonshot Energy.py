#Stephen Bauman
#PH230-Moonshot Energy
#3-4-10

from visual import *
from visual.graph import *
dt=5 #time step in seconds
G=6.673e-11 #N(m**2)/kg**2
dEM=4e8 #m
f=frame()

Earth=sphere(pos=(0,0,0),radius=6.4e6,color=color.blue)
Earth.mass= 6.e24 #kg
Earth.Work=0. #J

Moon=sphere(pos=(4e8,0,0),radius=1.75e6)
Moon.mass= 7.0e22 #kg
Moon.Work=0. #J

Naboo=sphere(pos=(50000.+6.4e6,0,0),radius=4e6,color=color.yellow)
Naboo.mass= 173 #kg
Naboo.speed= 1.3e4 #m/s
Naboo.P=Naboo.mass*Naboo.speed #kg m/s

KEi=.5*Naboo.mass*(Naboo.speed**2) #J

graph1=gcurve(color=color.yellow)
graph2=gcurve(color=color.green)
graph3=gcurve(color=color.cyan)
t=0 #s

while(Naboo.pos.x<(dEM-Moon.radius)):
    rESC= mag(Earth.pos-Naboo.pos) #m
    rMSC= mag(Moon.pos-Naboo.pos) #m
    Earth.Force=-G*Earth.mass*Naboo.mass/rESC**2 #N
    Moon.Force=G*Moon.mass*Naboo.mass/rMSC**2 #N
    Naboo.P=Naboo.P+(Earth.Force+Moon.Force)*dt #kg m/s**2
    Naboo.pos.x=Naboo.pos.x+Naboo.P/Naboo.mass*dt #m
    Earth.PE=(-G*Naboo.mass*Earth.mass)/mag(Earth.pos-Naboo.pos)
    Moon.PE=(-G*Naboo.mass*Moon.mass)/mag(Moon.pos-Naboo.pos)
    KEf=.5*Naboo.mass*((Naboo.P/Naboo.mass)**2) #J
    Naboo.dx=(Naboo.P/Naboo.mass*dt)#-50000+6.4e6
    Earth.Work=Earth.Work+Earth.Force*Naboo.dx #J
    Moon.Work=Moon.Work+Moon.Force*Naboo.dx #J
    f.pos.x=Naboo.pos.x
    scene.center=f.pos
    t=t+dt

    KEf=.5*Naboo.mass*((Naboo.P/Naboo.mass)**2) #J
    TotalPE=Earth.PE+Moon.PE
    TotalKE=KEf
    TotalE=TotalKE+TotalPE
    
    graph1.plot(pos=(rESC,TotalPE))
    graph2.plot(pos=(rESC, TotalKE))
    graph3.plot(pos=(rESC, TotalE))

print "Earth Work= ",Earth.Work,"J\n"
print "Moon Work= ",Moon.Work,"J\n"
print "Total Work=",Earth.Work+Moon.Work,"J\n"
print "Change in KE= ",KEf-KEi,"J"
