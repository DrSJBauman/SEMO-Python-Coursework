#Stephen Bauman
#PH230-01 Rutherford Experiment
#4-20-10

from visual import *

b = 15e-15 # Impact parameter -- change this to get different scattering angles

# Objects
Alpha = sphere(pos=(-2e-13,b,0), radius=2e-15, color=color.cyan)
Gold = sphere(pos=(0,0,0), radius=8e-15, color=color.yellow) 
Alpha.trail=curve(color=Alpha.color)
Gold.trail=curve(color=Gold.color)

# Constants and data
ProtonMass=1.67262158e-27 # kg
Alpha.mass = 4 * ProtonMass  #kg
Gold.mass = 197 * ProtonMass  #kg 
deltat = 1e-24  # seconds
t = 0       # seconds; Start counting time at zero
ElectronCharge=1.60217676e-19 # coulumbs
Alpha.charge = (2 * ElectronCharge) # coulumbs
Gold.charge = (79 * ElectronCharge) # coulumbs
Alpha.velocity = vector(2.19e7,0,0) # m/s

# Initial values
Alpha.p = Alpha.velocity * Alpha.mass # kg m/s
Gold.p = vector(0,0,0) * Gold.mass # kg m/s

scene.autoscale = 0     # Don't let camera zoom in and out as alpha moves

# Calculation loop
while t < (3 * 9.11e-21):
    # Calculate force on alpha particle by gold nucleus
    r = Alpha.pos - Gold.pos #Distance between Alpha particle and Gold nucleus
    rmag = mag(r)
    rhat = norm(r)
    FonA = (9e9 * ((Alpha.charge * Gold.charge * rhat)/(rmag**2))) # N
    
    # Calculate force on gold nucleus by alpha particle
    FonG = -(FonA)
    # Update the momentum of both alpha particle and gold nucleus
    Alpha.p = Alpha.p + (FonA * deltat)
    Gold.p = Gold.p + (FonG * deltat)
    
    # Update position of both alpha particle and gold nucleus
    Alpha.pos = Alpha.pos + (Alpha.p/Alpha.mass) * deltat # meters
    Gold.pos = Gold.pos + (Gold.p/Gold.mass) * deltat # meters
    
    Alpha.trail.append(pos=Alpha.pos) # Update trails
    Gold.trail.append(pos=Gold.pos)
   
    t = t + deltat  # Update time

    Alpha.Energy = .5 * Alpha.mass * mag((Alpha.p/Alpha.mass))**2 # J
    Gold.Energy = .5 * Gold.mass * mag((Gold.p/Gold.mass))**2 # J
    U = ((9e9 * ((Alpha.charge * Gold.charge)/(rmag))))
