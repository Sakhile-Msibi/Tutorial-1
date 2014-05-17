import math
import numpy as np
from matplotlib import pyplot as plt


def conv(f,g):
	assert(f.size==g.size)
	x=np.zeros(2*f.size)
	x[0:f.size]=f
	y=np.zeros(2*g.size)
	y[0:g.size]=g
	ff=np.fft.fft(x)
	gf=np.fft.fft(y)
	vec = np.real(np.fft.ifft(ff*gf))
	return vec[0:f.size]

x=np.arange(-20,20,0.1)
sigma = 2
y=np.exp(-0.5*x**2/sigma**2)

y=y/y.sum() 

yconv=conv(y,y)

plt.plot(x,y)
plt.plot(x,yconv)
plt.show()

