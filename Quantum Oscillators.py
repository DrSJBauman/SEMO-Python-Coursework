#Stephen Bauman
#PH230-01 Quantum Oscillators
#4-29-10

from visual import *
from visual.graph import *
from visual.factorial import*

N1=300 # Number of oscillators in block 1
N2= 200 # Number of oscillators in block 2
quanta=100 # Total number of quanta
k=1.38e-23 # J/K  Boltzmann constant

# Creates 2 graphs (gdisplays) with separate things on each
graph1=gdisplay(title='graph',xtitle='quanta',ytitle='S',
                foreground=color.green,background=color.black)
graph1=gcurve(color=color.red) 
graph2=gcurve(color=color.blue)
graph3=gcurve(color=color.white)

Histogram=gdisplay(title='Histogram',xtitle='quanta',ytitle='total ways',
                   foreground=color.green,background=color.black)
graph4=gvbars(color=color.orange)

for q in range(0,101,1):
    omega1=combin(q+N1-1,q) # Number of ways quanta can be arranged in block 1
    omega2=combin(q+N2-1,quanta-q) # Number of ways for block 2
    omega=omega1*omega2  # Total number of ways of the system
    S1=k*math.log(omega1) # Entropy of block 1
    S2=k*math.log(omega2) # Entropy of block 2
    S=S1+S2 # Total Entropy of system

    graph1.plot(pos=(q,S1))
    graph2.plot(pos=(q,S2))
    graph3.plot(pos=(q,S))
    graph4.plot(pos=(q,omega1*omega2)) #Plots histogram
