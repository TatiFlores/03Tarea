'''
Este script resuelve la edo resultante al realizar un cambio de variable a la
ecuacion del oscilador de van der Pool, mediante el metodo de Runge Kutta 3
'''

import numpy as np
import matplotlib.pyplot as plt


def f(y, v):
    return  v, (-1.795 * (y**2 - 1) * v - y)

def get_k1(y_n, v_n, h, f):
    f_eval = f(y_n, v_n)
    return h * f_eval[0], h * f_eval[1]

def get_k2(y_n, v_n, h, f):
    k1 = get_k1(y_n, v_n, h, f)
    f_eval = f(y_n + h/2, v_n + k1[1]/2)
    return h * f_eval[0], h * f_eval[1]

def get_k3(y_n, v_n, h, f):
    k1 = get_k1(y_n, v_n, h, f)
    k2 = get_k2(y_n, v_n, h, f)
    f_eval = f(y_n + h, v_n - k1[1] - 2*k2[1])
    return h * f_eval[0], h * f_eval[1]

def rk3_step(y_n, v_n, h, f):
    k1 = get_k1(y_n, v_n, h, f)
    k2 = get_k2(y_n, v_n, h, f)
    k3 = get_k3(y_n, v_n, h, f)
    y_n1 = y_n + (k1[0] + 4 * k2[0] + k3[0])/6
    v_n1 = v_n + (k1[1] + 4 * k2[1] + k3[1])/6
    return y_n1, v_n1

N_steps = 40000
h = 20*np.pi / N_steps
y_caso1 = np.zeros(N_steps)
v_caso1 = np.zeros(N_steps)

y_caso1[0] = 0.1
v_caso1[0] = 0
for i in range(1, N_steps):
    y_caso1[i], v_caso1[i] = rk3_step(y_caso1[i-1], v_caso1[i-1], h, f)

y_caso2 = np.zeros(N_steps)
v_caso2 = np.zeros(N_steps)

y_caso2[0] = 4
v_caso2[0] = 0
for i in range(1, N_steps):
    y_caso2[i], v_caso2[i] = rk3_step(y_caso2[i-1], v_caso2[i-1], h, f)

s_rk = [h * i for i in range(N_steps)]

plt.figure(1)
plt.plot(s_rk, y_caso1, 'b')
plt.xlabel('$s$', fontsize=18)
plt.ylabel('$y(s)$', fontsize=18)
plt.savefig("Caso1ys.eps")

plt.figure(2)
plt.plot(s_rk, y_caso2, 'g')
plt.xlabel('$s$', fontsize=18)
plt.ylabel('$y(s)$', fontsize=18)#, fontsize=18)
plt.savefig("Caso2ys.eps")

plt.figure(3)
plt.plot(y_caso1,v_caso1,'b')
plt.xlabel('$y (s)$', fontsize=18)
plt.ylabel('$dy/ds$', fontsize=18)
plt.savefig("Caso1dydsys.eps")

plt.figure(4)
plt.plot(y_caso2,v_caso2,'g')
plt.xlabel('$y (s)$', fontsize=18)
plt.ylabel('$dy/ds$', fontsize=18)
plt.savefig("Caso1dydsys.eps")

plt.show()
plt.draw()
