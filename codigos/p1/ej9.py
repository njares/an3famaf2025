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

# Ejemplos de formas de calcular las normas para los errores
# Por ejemplo, para el tercer error
# f: la función sin ruido
# df: la derivada exacta de f

x = np.linspace(-1,1,100)

# Error como la suma de desviaciones, es un múltiplo de la norma 1
E_3 = np.sum(np.abs(df(x) - f_diff_gauss_legendre(x, f, h, n)))

# Norma 1 con quad
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html
from scipy.integrate import quad

diff = lambda x : np.abs(df(x) - f_diff_gauss_legendre(x, f, h, n))
E_3 = quad(diff, -1, 1)[0]
