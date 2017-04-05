from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(2)

n = 256
t = np.arange(n)
line, = ax[0].plot(t, np.zeros(n))
line2, = ax[1].plot(t, np.zeros(n))
lines = [line, line2]
ax[0].set_ylim([0,1])
ax[1].set_xlim([0,1])
ax[1].set_ylim([-.25,1])

def getLogisticMap(r):
	y = np.zeros(n)
	y[0] = .5
	for i in np.arange(n):
		if i > 0:
			y[i] = r * y[i-1] * (1 - y[i-1])
	return y

def animate(i):
	m = getLogisticMap(i)
	lines[0].set_ydata(m)  # update the data
	fourier = np.fft.fft(m)
	xf = np.linspace(0.0, 1.0, n)

	lines[1].set_data(xf, 2.0/n * np.abs(fourier[:n]))
	return lines


# Init only required for blitting to give a clean slate.
def init():
    lines[0].set_ydata(np.ma.array(t, mask=True))
    lines[1].set_ydata(np.ma.array(t, mask=True))
    return lines

ani = animation.FuncAnimation(fig, animate, np.arange(1, 5, .0125), init_func=init,
                              interval=100, blit=True)
plt.show()