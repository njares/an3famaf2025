import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(x, U, duracion, formato, xlim, ylim, filename=None):
	# fig = plt.figure(figsize=(5, 4))
	fig = plt.figure()
	ax = fig.add_subplot(autoscale_on=False, xlim=xlim, ylim=ylim)
	#ax = fig.add_subplot()
	# ax.set_aspect('equal')
	# ax.grid()
	line, = ax.plot([], [], 'o-', lw=2)
	def animate_line(k):
		line.set_data(x, U[:,k])
		#plot(x, U[:,k])
		return (line,)
	ani = animation.FuncAnimation(
		fig, animate_line, U.shape[1], interval=duracion*1000/U.shape[1], blit=True)
	if formato =='plot':
		plt.show()
	elif formato == 'avi':
		if not filename:
			filename = "animacion_pyplot.avi"
		ani.save(filename)
	else:
		print("formato inválido")
		return None
