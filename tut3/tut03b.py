import numpy as np
import scipy
from matplotlib import pyplot as plt

def corr(f,g):
	ff=np.fft.fft(f)
	gf=np.fft.fft(g)
	gfconj=np.conj(gf)
	return np.real(np.fft.ifft(ff*gfconj))


x=np.arange(-40,40,0.2)
sigma=2
y=np.exp(-0.5*x**2/sigma**2)

cor=corr(y,y)
plt.plot(x,cor)
plt.show()
