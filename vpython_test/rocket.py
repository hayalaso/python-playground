from vpython import *
import numpy as np
import matplotlib.pyplot as plt

def density_air(h):
    """
    Density Model from https://www.grc.nasa.gov/www/k-12/airplane/atmosmet.html
    """
    if h > 25000:
        T = -131.21 + 0.00299*h
        p = 2.488 * ((T+273.11)/216.6)**(-11.38)
    elif h < 11000:
        T = 15.04 - 0.00649*h
        p = 101.29 * ((T+273.11)/288.08)**(5.256)
    else:
        T = -56.46 
        p = 22.65*np.exp(1.73-0.000157*h)
    return p/(0.2869*(T+273.11))
    
tgraph = graph(title='Deorbit',xtitle='Time [s]', ytitle = 'Altitude [m]')
f1 = gcurve(color=color.blue)

r_rocket = 2.5
A_rocket = np.pi*(r_rocket**2) #m2 
m_rocket = 200 #kg
C = 0.8
G = 6.67e-11
M_earth = 5.972e24 #kg
R_earth = 6.371e6

h_rocket = 300e3

earth = sphere(pos=vector(0,0,0),radius=R_earth,texture=textures.earth)
rocket = sphere(pos=vector(R_earth+h_rocket,0,0),radius=R_earth/40.,color=color.red,make_trail=True)

v0 = 0.999*sqrt(G*M_earth/(R_earth+h_rocket))
rocket.m = m_rocket
rocket.p = rocket.m*vector(0,0,v0)

t=0.
dt=1.0 #sec
while mag(rocket.pos)>R_earth:
    rate(1000)
    
    r = rocket.pos - earth.pos  
    rocket.v = rocket.p/rocket.m
    h = mag(r)-R_earth
    F = - G*M_earth*rocket.m*norm(r)/mag(r)**2 - 0.5*density_air(h)*A_rocket*C*norm(rocket.v)*mag(rocket.v)**2
    rocket.p = rocket.p + F*dt
    rocket.pos = rocket.pos + rocket.p*dt/rocket.m
    t+=dt
    f1.plot(t, h)

theta = atan2(r.y,r.x)*180/np.pi
print(t, theta)
