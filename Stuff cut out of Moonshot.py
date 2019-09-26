#stuff cut out of Moonshot

SatellitewingTR=box(pos=(Satellite.pos.x+4e6,Satellite.pos.y+4e6,Satellite.pos.z+12e6),size=(4e6,1e6,1e6),color=color.red)
SatellitewingTL=box(pos=(Satellite.pos.x+4e6,Satellite.pos.y+4e6,Satellite.pos.z-12e6),size=(4e6,1e6,1e6),color=color.red)
SatellitewingBL=box(pos=(Satellite.pos.x+4e6,Satellite.pos.y-4e6,Satellite.pos.z-12e6),size=(4e6,1e6,1e6),color=color.red)
SatellitewingBR=box(pos=(Satellite.pos.x+4e6,Satellite.pos.y-4e6,Satellite.pos.z+12e6),size=(4e6,1e6,1e6),color=color.red)

SatellitewingTRpoint=arrow(pos=(Satellite.pos.x+4e6,Satellite.pos.y+4e6,Satellite.pos.z+12e6),axis=(8e6,0,0),color=color.red,shaftwidth=.25e6)
                                
Satellitewing1=box(pos=Satellite.pos,axis=(SatellitewingTR.pos-SatellitewingBL.pos), width=4e6,height=1e6,color=color.red)
Satellitewing2=box(pos=Satellite.pos,axis=(SatellitewingTL.pos-SatellitewingBR.pos),width=4e6,height=1e6,color=color.red)
Satellitebody=box(pos=Satellite.pos, size=(8e6,6e6,6e6), color=color.white)
Satellitenose=pyramid(pos=(Satellite.pos.x+8e6,0,0),size=(30e6,6e6,6e6))


    Satellitewing1.pos=Satellite.pos
    Satellitewing2.pos=Satellite.pos
    SatellitewingTR.pos.x=Satellite.pos.x+4e6
    SatellitewingTL.pos.x=Satellite.pos.x+4e6
    SatellitewingBL.pos.x=Satellite.pos.x+4e6
    SatellitewingBR.pos.x=Satellite.pos.x+4e6
    Satellitebody.pos.x=Satellite.pos.x+8e6
    Satellitenose.pos.x=Satellite.pos.x
    SatellitewingTRpoint.pos.x=Satellite.pos.x+4e6
