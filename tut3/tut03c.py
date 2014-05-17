import numpy as np
import scipy
from matplotlib import pyplot as plt

def shift(arr,i=0):
	vector = 0*arr;
	vector[i]=1
	arrft = np.fft.fft(arr)
	vft=np.fft.fft(vector)
	return np.real(np.fft.ifft(arrft*vft))

def corr(f,g):
	ff=np.fft.fft(f)
	gf=np.fft.fft(g)
	gfconj=np.conj(gf)
	return np.real(np.fft.ifft(ff*gfconj))


x=np.arange(-40,40,0.2)
sigma=2
y=np.exp(-0.5*x**2/sigma**2)

cor=corr(y,y)
yshift=shift(y,y.size/3)
ycor=corr(yshift,yshift)

mean = np.mean(np.abs(cor-ycor))

print "Mean diff : "+ repr(mean)

plt.plot(x,cor)
plt.plot(x,ycor)
plt.show()
