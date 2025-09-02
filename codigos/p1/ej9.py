import numpy as np
from scipy.special import roots_legendre
import matplotlib.pyplot as plt

# Ejemplo de cuadratura de Gauss Legendre

def g_aprox_gauss_legendre(x,f,h,n):
	x_nodes, w = roots_legendre(n)
	f_u = lambda u : u*f(h*u + x)
	return f_u(x_nodes).dot(w)

def f_diff_gauss_legendre(x,f,h,n):
	return (3/( 2*h ))*g_aprox_gauss_legendre(x,f,h,n)
