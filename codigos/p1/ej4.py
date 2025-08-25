import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.sin(np.pi * x)

h_list = [0.2, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001]

def diff_back(f, x0, h):
	return (f(x0)-f(x0-h))/h

def f_prima_exacta(x):
	return np.cos(np.pi * x) * np.pi

#x0 = 0.4
x0 = 1.0

error_list = []

for h in h_list:
	error_list.append(np.abs(f_prima_exacta(x0) - diff_back(f, x0, h)))

p_estimado = []

for i in range(len(h_list)-1):
	p_estimado.append(np.log(error_list[i] / error_list[i+1]) / np.log(h_list[i] / h_list[i+1]))

plt.plot(p_estimado)
plt.ylim(-0.5, 2.5)

plt.show()
