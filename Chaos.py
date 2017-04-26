from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(3)

n = 128
t = np.arange(n)
line, = ax[0].plot(t, np.zeros(n))
line2, = ax[1].plot(t, np.zeros(n))
lines = [line, line2]
ax[0].set_ylim([0, 1])
rateText = plt.text(.8, .1, 0, bbox=dict(facecolor='white', alpha=1), transform=ax[0].transAxes)
ax[1].set_xlim([0, 1])
ax[1].set_ylim([-.25, 1])
ax[2].set_xlim([0, 4])
ax[2].set_ylim([0, 1])

def getLogisticMap(r, n):
	y = np.zeros(n)
	y[0] = .5
	for i in np.arange(n):
		if i > 0:
			y[i] = r * y[i-1] * (1 - y[i-1])
	return y

def bifurcation():
	for r in np.arange(0, 4, 4/1000):
		ys = getLogisticMap(r, 200)
		ys = ys[100:]
		ax[2].scatter([r] * len(ys), ys, s=[.5]*len(ys), marker='.', color='blue')

def animate(i):
	m = getLogisticMap(i, n)
	lines[0].set_ydata(m)  # update the data
	rateText.set_text(i)
	fourier = np.fft.fft(m)
	xf = np.linspace(0.0, 1.0, n)

	lines[1].set_data(xf, 2.0/n * np.abs(fourier[:n]))
	return lines[0], lines[1], rateText


# Init only required for blitting to give a clean slate.
def init():
    lines[0].set_ydata(np.ma.array(t, mask=True))
    lines[1].set_ydata(np.ma.array(t, mask=True))
    return lines

bifurcation()
timing = np.arange(1, 3.5, 0.0125)
timing = np.hstack((timing, np.arange(3.5, 4.05, 0.002)))
ani = animation.FuncAnimation(fig, animate, timing, init_func=init,
                              interval=100, blit=True)
plt.show()