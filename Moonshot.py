#Stephen Bauman
#PH230-Moonshot
#3-4-10

from visual import *
from visual.graph import *
dt=.75 #time step in seconds
G=6.7e-11 #N(m**2)/kg**2
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

#=================================================

Naboobody= cylinder(frame=f, pos=(Naboo.pos.x-6e6,0,0), axis=(19e6,0,0), radius=4e6,color=color.yellow)
Naboonose= cone(frame=f, pos=(Naboobody.pos.x+Naboobody.axis.x,0,0), axis=(12e6,0,0), radius=4e6, color=color.yellow)
Naboonose2= ellipsoid(frame=f, pos=(Naboonose.pos.x,-.75e6,0), length=30e6, height=4e6, width=18e6, color=color.white)
Naboonose3= ellipsoid(frame=f, pos=(Naboonose.pos.x,-.35e6,0), length=28e6, height=4e6, width=16e6, color=color.white)
Naboonose4= ellipsoid(frame=f, pos=(Naboonose.pos.x,-.15e6,0), length=26e6, height=4e6, width=18e6, color=color.yellow)
Naboonose4= ellipsoid(frame=f, pos=(Naboonose.pos.x,.05e6,0), length=24e6, height=4e6, width=18e6, color=color.yellow)
Naboocockpit= ellipsoid(frame=f, pos=(Naboobody.pos.x+6e6,3e6,0), length = 12e6, height=6e6, width= 4e6, color=color.cyan)
Nabootail= pyramid(frame=f, pos=(Naboobody.pos.x-2.3e6,1.5e6,0), axis=(-50e6,7e6,0), size=(40e6, 3.5e6, 3.5e6), color=color.yellow)
R2D2= cylinder(frame=f, pos=(Naboobody.pos.x,3.7e6,0), axis=(0,2.3e6,0), radius=1e6, color=color.white)
R2D2head= sphere(frame=f, pos=(Naboobody.pos.x,3.7e6+2.3e6,0), radius=1e6, color=color.white)
R2D3eye= sphere(frame=f, pos=(Naboobody.pos.x+.8e6,3.7e6+2.7e6,.4e6), radius=.1e6, color=color.blue)
R2D2seat= cylinder(frame=f, pos=(Naboobody.pos.x,3.7e6,0), axis=(0,1.8e6,0), radius=1.1e6, color=color.yellow)

NaboowingR= box(frame=f, pos=(Naboonose2.pos.x+9e6,Naboonose.pos.y-1e6,14.5e6), axis=(-8e6,-1e6,30e6), width=3e6, height=.5e6, color=color.white)
NaboowingL= box(frame=f, pos=(Naboonose2.pos.x+9e6,Naboonose.pos.y-1e6,-14.5e6), axis=(-8e6,-1e6,-30e6), width=3e6, height=.5e6, color=color.white)
NaboowingRB= box(frame=f, pos=(Naboonose.pos.x+6e6,Naboonose.pos.y-1e6,15e6), axis=(-2e6,-1e6,26e6), width=5e6, height=.5e6, color=color.yellow)
NaboowingLB= box(frame=f, pos=(Naboonose.pos.x+6e6,Naboonose.pos.y-1e6,-15e6), axis=(-2e6,-1e6,-26e6), width=5e6, height=.5e6, color=color.yellow)

NabooBoosterR1= cylinder(frame=f, pos=(Naboonose.pos.x-1e6,Naboonose.pos.y-1e6,30e6), axis=(5e6, 0,0), radius=3e6, color=color.yellow)
NabooBoosterR2= sphere(frame=f, pos=(Naboonose.pos.x-1.25e6,Naboonose.pos.y-1e6,30e6), axis=(5e6, 0,0), radius=3e6, color=color.yellow)
NabooBoosterR3= cylinder(frame=f, pos=(Naboonose.pos.x+3.5e6,Naboonose.pos.y-1e6,30e6), axis=(10e6, 0,0), radius=3e6, color=color.white)
NabooBoosterR4= cone(frame=f, pos=(Naboonose.pos.x+13.5e6,Naboonose.pos.y-1e6,30e6), axis=(5e6, 0,0), radius=2.7e6, color=color.white)
NabooBoosterR5= ring(frame=f, pos=(Naboonose.pos.x+13.5e6,Naboonose.pos.y-1e6,30e6), axis=(5e6, 0,0), radius=2.7e6, thickness=.25e6, color=color.yellow)
NabooBoosterR6= cone(frame=f, pos=(Naboonose.pos.x-3e6,Naboonose.pos.y-1e6,30e6), axis=(-5e6, 0,0), radius=2e6, color=color.blue)
NabooBoosterR7= pyramid(frame=f, pos=(Naboonose.pos.x-7e6,Naboonose.pos.y-1e6,30e6), axis=(-30e6,0,0), size=(10e6,.5e6,.5e6), color=color.blue)

NabooBoosterL1= cylinder(frame=f, pos=(Naboonose.pos.x-1e6,Naboonose.pos.y-1e6,-30e6), axis=(5e6, 0,0), radius=3e6, color=color.yellow)
NabooBoosterL2= sphere(frame=f, pos=(Naboonose.pos.x-1.25e6,Naboonose.pos.y-1e6,-30e6), axis=(5e6, 0,0), radius=3e6, color=color.yellow)
NabooBoosterL3= cylinder(frame=f, pos=(Naboonose.pos.x+3.5e6,Naboonose.pos.y-1e6,-30e6), axis=(10e6, 0,0), radius=3e6, color=color.white)
NabooBoosterL4= cone(frame=f, pos=(Naboonose.pos.x+13.5e6,Naboonose.pos.y-1e6,-30e6), axis=(5e6, 0,0), radius=2.7e6, color=color.white)
NabooBoosterL5= ring(frame=f, pos=(Naboonose.pos.x+13.5e6,Naboonose.pos.y-1e6,-30e6), axis=(5e6, 0,0), radius=2.7e6, thickness=.25e6, color=color.yellow)
NabooBoosterL6= cone(frame=f, pos=(Naboonose.pos.x-3e6,Naboonose.pos.y-1e6,-30e6), axis=(-5e6, 0,0), radius=2e6, color=color.blue)
NabooBoosterL7= pyramid(frame=f, pos=(Naboonose.pos.x-7e6,Naboonose.pos.y-1e6,-30e6), axis=(-30e6,0,0), size=(10e6,.5e6,.5e6), color=color.blue)

#=================================================

#graph=gcurve(color=color.yellow)
KEi=.5*Naboo.mass*(Naboo.speed**2) #J
t=0 #s

while(Naboo.pos.x<(dEM-Moon.radius)):
    rESC= mag(Earth.pos-Naboo.pos) #m
    rMSC= mag(Moon.pos-Naboo.pos) #m
    Earth.Force=-G*Earth.mass*Naboo.mass/rESC**2 #N
    Moon.Force=G*Moon.mass*Naboo.mass/rMSC**2 #N
    Naboo.P=Naboo.P+(Earth.Force+Moon.Force)*dt #kg m/s**2
    #Naboo.dx=(Naboo.P/Naboo.mass*dt)-pos(50000+6.4e6,0,0)
    Naboo.pos.x=Naboo.pos.x+Naboo.P/Naboo.mass*dt #m
    Earth.Work=Earth.Work+Earth.Force*rESC #J
    Moon.Work=Moon.Work+Moon.Force*rMSC #J

#======================================================

    f.pos.x=Naboo.pos.x

#======================================================

    t=t+dt
    #graph.plot(pos=(t,Naboo.P/Naboo.mass))
    scene.center=f.pos

KEf= Earth.Work + Moon.Work + KEi #J
print "Earth Work= ",Earth.Work,"J\n"
print "Moon Work= ",Moon.Work,"J\n"
print "Total Work=",Earth.Work+Moon.Work,"J\n"
print "Change in K= ",KEf-KEi,"J"
