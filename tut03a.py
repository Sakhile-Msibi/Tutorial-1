from numpy.fft import fft,ifft
import numpy as np
from matplotlib import pyplot as plt

def conv(x,y):
    assert(x.size==y.size) 
    xx=np.zeros(2*x.size)
    xx[0:x.size]=x

    yy=np.zeros(2*y.size)
    yy[0:y.size]=y
    xxft=fft(xx)
    yyft=fft(yy)
    vec=np.real(ifft(xxft*yyft))
    return vec[0:x.size]

def shift(x,n=0):
    vec=0*x 
    vec[n]=1
    vecb=fft(vec)
    xft=fft(x)
    return np.real(ifft(xft*vecb))


x=np.arange(-40,40,0.2)
sigma=2
y=np.exp(-0.5*x**2/sigma**2)
yshift=shift(y,y.size/2)
    
yconv=conv(y,y)
plt.plot(x,y)
plt.plot(x,yshift)
