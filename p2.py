'''
Este codigo resuelve la ecuacion de Lorentz
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D

def funcion(t, p):
    dx = 10 * (p[1] - p[0])
    dy = p[0] * (28 - p[2]) - p[1]
    dz = p[0] * p[1] - p[2]*(8./3)
    return [dx,dy,dz]

#Condiciones iniciales
t0 = 0.0001 #Cambiar por 0.0001 si no funciona
x0 = 1
y0 = 1
z0 = 1
p0 = [x0, y0, z0]
