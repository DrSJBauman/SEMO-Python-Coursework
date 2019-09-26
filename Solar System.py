from visual import *
AUE=1.5e11 #m
G=6.7e-11 #N*m^2/kg^2
speedE=2*pi*AUE/31536000.0 #m/s
dt=1000 #s
vscale=10000
trailE=curve(color=color.blue)
sun = sphere(pos=(0.,0.,0.), radius=vscale*3999999., color=color.yellow)
sun.mass=1.98892e30 #kg
Earth = sphere(pos=(AUE,0.,0.), radius=vscale*637800.1, color=color.blue)
Earth.mass=5.9742e24 #kg
Earth.velocity=vector(0,speedE,0) #m/s
Earth.P=Earth.mass*Earth.velocity #kg m/s^2
Farrow=arrow(pos=Earth.pos, axis=sun.pos-Earth.pos, color=color.red)
Parrow=arrow(pos=Earth.pos, axis=Earth.velocity, color=color.orange)

scene.center=(sun.pos)
scene.autoscale=0

AUV=1.082e11 #m
speedV=2*pi*AUV/19409760.0 #m/s
trailV=curve(color=color.magenta)
Venus = sphere(pos=(AUV,0.,0.), radius=vscale*605100.8, color=color.magenta)
Venus.mass=4.869e24 #kg
Venus.velocity=vector(0,speedV,0) #m/s
Venus.P=Venus.mass*Venus.velocity #kg m/s^2

AUME=5.79e10 #m
speedME=2*pi*AUME/7600521.6 #m/s
trailME=curve(color=color.orange)
Mercury = sphere(pos=(AUME,0.,0.), radius=vscale*243900.8, color=color.orange)
Mercury.mass=3.3e23 #kg
Mercury.velocity=vector(0,speedME,0) #m/s
Mercury.P=Mercury.mass*Mercury.velocity #kg m/s^2

AUMA=2.279e11 #m
speedMA=2*pi*AUMA/59355072.0 #m/s
trailMA=curve(color=color.red)
Mars = sphere(pos=(AUMA,0.,0.), radius=vscale*339700.0, color=color.red)
Mars.mass=6.42e23 #kg
Mars.velocity=vector(0,speedMA,0) #m/s
Mars.P=Mars.mass*Mars.velocity #kg m/s^2

AUJ=7.783e11 #m
speedJ=2*pi*AUJ/37423136.0 #m/s
trailJ=curve(color=color.white)
Jupiter = sphere(pos=(AUJ,0.,0.), radius=vscale*7140000.0)
Jupiter.mass=1.90e27 #kg
Jupiter.velocity=vector(0,speedJ,0) #m/s
Jupiter.P=Jupiter.mass*Jupiter.velocity #kg m/s^2

AUS=1.426e12 #m
speedS=2*pi*AUS/928109016.0 #m/s
trailS=curve(color=color.green)
Saturn = sphere(pos=(AUS,0.,0.), radius=vscale*6000000.0, color=color.green)
Saturn.mass=5.69e26 #kg
Saturn.velocity=vector(0,speedS,0) #m/s
Saturn.P=Saturn.mass*Saturn.velocity #kg m/s^2

AUU=2.871e12 #m
speedU=2*pi*AUU/2652100704.0 #m/s
trailU=curve(color=color.magenta)
Uranus = sphere(pos=(AUU,0.,0.), radius=vscale*2556000.0, color=color.magenta)
Uranus.mass=8.7e25 #kg
Uranus.velocity=vector(0,speedU,0) #m/s
Uranus.P=Uranus.mass*Uranus.velocity #kg m/s^2

AUN=4.497e12 #m
speedN=2*pi*AUN/5200692480.0 #m/s
trailN=curve(color=color.cyan)
Neptune = sphere(pos=(AUN,0.,0.), radius=vscale*247600.0, color=color.cyan)
Neptune.mass=1.03e26 #kg
Neptune.velocity=vector(0,speedN,0) #m/s
Neptune.P=Neptune.mass*Neptune.velocity #kg m/s^2

while(1):
    rseE=Earth.pos-sun.pos
    ForceE=-G*sun.mass*Earth.mass*rseE/mag(rseE)**3
    Earth.P=Earth.P+ForceE*dt
    Earth.pos=Earth.pos+Earth.P/Earth.mass*dt
    trailE.append(pos=Earth.pos)
    Farrow.pos=Earth.pos
    Parrow.pos=Earth.pos
    Farrow.axis=ForceE/1.e12
    Parrow.axis=Earth.P/1.e18/4.25

    rseV=Venus.pos-sun.pos
    ForceV=-G*sun.mass*Venus.mass*rseV/mag(rseV)**3
    Venus.P=Venus.P+ForceV*dt
    Venus.pos=Venus.pos+Venus.P/Venus.mass*dt
    trailV.append(pos=Venus.pos)

    rseME=Mercury.pos-sun.pos
    ForceME=-G*sun.mass*Mercury.mass*rseME/mag(rseME)**3
    Mercury.P=Mercury.P+ForceME*dt
    Mercury.pos=Mercury.pos+Mercury.P/Mercury.mass*dt
    trailME.append(pos=Mercury.pos)

    rseMA=Mars.pos-sun.pos
    ForceMA=-G*sun.mass*Mars.mass*rseMA/mag(rseMA)**3
    Mars.P=Mars.P+ForceMA*dt
    Mars.pos=Mars.pos+Mars.P/Mars.mass*dt
    trailMA.append(pos=Mars.pos)

    #rseJ=Jupiter.pos-sun.pos
    #ForceJ=-G*sun.mass*Jupiter.mass*rseJ/mag(rseJ)**3
    #Jupiter.P=Jupiter.P+ForceJ*dt
    #Jupiter.pos=Jupiter.pos+Jupiter.P/Jupiter.mass*dt
    #trailJ.append(pos=Jupiter.pos)
    
    rseS=Saturn.pos-sun.pos
    ForceS=-G*sun.mass*Saturn.mass*rseS/mag(rseS)**3
    Saturn.P=Saturn.P+ForceS*dt
    Saturn.pos=Saturn.pos+Saturn.P/Saturn.mass*dt
    trailS.append(pos=Saturn.pos)

    rseU=Uranus.pos-sun.pos
    ForceU=-G*sun.mass*Uranus.mass*rseU/mag(rseU)**3
    Uranus.P=Uranus.P+ForceU*dt
    Uranus.pos=Uranus.pos+Uranus.P/Uranus.mass*dt
    trailU.append(pos=Uranus.pos)

    rseN=Neptune.pos-sun.pos
    ForceN=-G*sun.mass*Neptune.mass*rseN/mag(rseN)**3
    Neptune.P=Neptune.P+ForceN*dt
    Neptune.pos=Neptune.pos+Neptune.P/Neptune.mass*dt
    trailN.append(pos=Neptune.pos)
