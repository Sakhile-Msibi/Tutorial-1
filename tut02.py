#1)
import numpy as np
import math
from matplotlib import pyplot as plt
def avec(n):
    x=np.arange(0,n)
    x=0.5*x*math.pi/(n-1)
    return x
#==========================================
#2)
def integrate_simple(n):
    dx=math.pi/2/n
    vec=avec(n)
    T=np.sum(np.cos(vec))
    return dx*T
#==========================================
#4)
def integrate_simpson(n):
    dx=math.pi/(n-1)
    vec=np.cos(avec(n))
#==========================================
#3)
    x_odd=vec[1:-1:2]
    x_even=vec[2:-1:2]
    T=np.sum(x_even)/3+np.sum(x_odd)*2/3+vec[0]/6+vec[-1]/6
    return T*dx
#==========================================
#2)
if __name__=='__main__':
    print '2)'
    felem=[10,30,100,300,1000]    
    for n in felem:
        bad_int=integrate_simple(n)
        print 'simple integrator with ' + repr(n) + ' points has value ' + repr(bad_int)
#===========================================
#4)
    print '4)'
    myval=integrate_simpson(5)
    myerr=np.abs(myval-1)
    print 'error is ' + repr(myerr-1)
    for n in felem:
        myerr=np.abs(integrate_simpson(n)-1)
        print 'simpsons error on' + repr(n) + ' is ' + repr(myerr)

#============================================
#5)
    print '5)'
    felem=[10,30,100,300,1000,3001,10001,30001,100001]
    felem=np.array(felem)
    simpson_err=np.zeros(felem.size)
    simple_err=np.zeros(felem.size)
    for ii in range(felem.size):
        n=felem[ii]
        simpson_err[ii]=np.abs(integrate_simpson(n)-1)
        simple_err[ii]=np.abs(integrate_simple(n)-1)
    plt.plot(felem,simple_err)
    plt.plot(felem,simpson_err)
    ax=plt.gca()

    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.show() 
