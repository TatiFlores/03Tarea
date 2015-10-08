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
