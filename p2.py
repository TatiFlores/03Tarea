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

r = ode(funcion)
r.set_integrator('dopri5')
r.set_initial_value(p0)

t_values = np.linspace(t0, 10* np.pi,10000)
x = np.zeros(len(t_values))
y = np.zeros(len(t_values))
z = np.zeros(len(t_values))

for i in range(len(t_values)):
    r.integrate(t_values[i])
    x[i], y[i] , z[i]= r.y

fig = plt.figure(1)

ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('equal')

ax.plot(x, y, z, 'k')

ax.set_title('Atractor de Lorenz')
ax.set_xlabel('x', fontsize=18)
ax.set_ylabel('y', fontsize=18)
ax.set_zlabel('z', fontsize=18)

plt.show()
plt.draw()
