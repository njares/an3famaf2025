import numpy as np
import matplotlib.pyplot as plt

from animation import animate

# u_t + u_x = 0
# -1 < x < 1
# 0 < t < 1
# u(x,0) = u_0(x)
# u(-1, t) = 0

u_0_1 = lambda x : (x+1)*np.exp(-x/2)

def u_0_2(x):
	if -.5 < x and x < .5:
		return 1
	return 0

# Up Wind

def up_wind(u0, m, n):
	dt = 1 / n
	h = 2 / m
	# defino el arreglo con la solución
	U = np.zeros((m+1,n+1))
	# guardo la solución inicial
	for j in range(m+1):
		U[j,0] = u0(-1 + h*j)
	# itero en el tiempo
	for k in range(n):
		# itero en el espacio
		# u(-1,t) = 0
		U[1,k+1] = U[1,k]*(1 - dt/h)
		for j in range(2,m+1):
			U[j, k+1] = U[j,k] * (1 - dt/h) + U[j-1,k] * (dt/h)
	x = np.linspace(-1, 1, m+1)
	return U, x

# Lax Wendroff

def lax_wendroff(u0, m, n):
	dt = 1 / n
	h = 2 / m
	# defino el arreglo con la solución
	U = np.zeros((m+1,n+1))
	# guardo la solución inicial
	for j in range(m+1):
		U[j,0] = u0(-1 + h*j)
	# itero en el tiempo
	for k in range(n):
		# itero en el espacio
		# u(-1,t) = 0
		U[1,k+1] = U[1,k] * ( - (dt/h)**2 +1 ) + U[2,k] * ( .5*(dt/h)**2  - .5*dt/h)
		for j in range(2,m):
			U[j, k+1] = U[j-1,k] * ( .5*(dt/h)**2  + .5*dt/h ) + U[j,k] * ( - (dt/h)**2 +1 ) + U[j+1,k] * (  .5*(dt/h)**2  - .5*dt/h )
		U[m,k+1] = U[m,k] * ( 1 - 1.5*dt/h + .5*(dt/h)**2 ) + U[m-1,k] * ( 2*dt/h - (dt/h)**2 ) + U[m-2,k] * ( .5*(dt/h)**2 - .5*dt/h )
	x = np.linspace(-1, 1, m+1)
	return U, x


m = 20
n = 10

U1_uw, x = up_wind(u_0_1, m, n)
U2_uw, x = up_wind(u_0_2, m, n)
U1_lw, x = lax_wendroff(u_0_1, m, n)
U2_lw, x_exact = lax_wendroff(u_0_2, m, n)
 
# for k in range(n+1):
# 	plt.plot(x, U1_lw[:,k])
# 	plt.show()

# plt.plot(x, U1_uw[:,-1], label = "cond 1, upwind")
# plt.plot(x, U2_uw[:,-1], label = "cond 2, upwind")
# plt.plot(x, U1_lw[:,-1], label = "cond 1, lax wend")
# plt.plot(x, U2_lw[:,-1], label = "cond 2, lax wend")
# 
# plt.legend()
# plt.show()

animate(x_exact, U1_uw, duracion=2, formato='plot', xlim=(-1.1, 1.1), ylim=(-.1, 1.5))
animate(x_exact, U2_uw, duracion=2, formato='plot', xlim=(-1.1, 1.1), ylim=(-.1, 1.5))
animate(x_exact, U1_lw, duracion=2, formato='plot', xlim=(-1.1, 1.1), ylim=(-.1, 1.5))
animate(x_exact, U2_lw, duracion=2, formato='plot', xlim=(-1.1, 1.1), ylim=(-.1, 1.5))
