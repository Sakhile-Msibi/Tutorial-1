import numpy
from matplotlib import pyplot as plt

def pivector(n):
    x=numpy.arange(0,n)
    x=0.5*x*numpy.pi/(n-1)
    return x

def integrate_cos_simple(n):
    dx=numpy.pi/2/n
    vec=pivector(n)
    tot=numpy.sum(numpy.cos(vec))
    return dx*tot

def integrate_cos_simpson(n):
    dx=numpy.pi/2/(n-1)*2

    vec=numpy.cos(pivector(n))
    #Question 3
    x_even=vec[2:-1:2]
    x_odd=vec[1:-1:2]
    tot=numpy.sum(x_even)/3+numpy.sum(x_odd)*2/3+vec[0]/6+vec[-1]/6
    return tot*dx

if __name__=='__main__':
    
    #Question 2
    print 'Question 2'
    mel=[10,30,100,300,1000,3000]    
    for n in mel:
        bad_int=integrate_cos_simple(n)
        print 'simple integrator with ' + repr(n) + ' points has value ' + repr(bad_int)

    #Question 4
    print 'Question 4'
    myval=integrate_cos_simpson(11)
    err=numpy.abs(myval-1)
    print 'error on 11 points is ' + repr(err-1)
    for n in mel:
        err=numpy.abs(integrate_cos_simpson(n)-1)
        print 'simpsons error on ' + repr(n) + ' is ' + repr(err)


    print 'Question 5'
    mel=[10,30,100,300,1000,3000]
    mel=numpy.array(mel)
    simpson_err=numpy.zeros(mel.size)
    simple_err=numpy.zeros(mel.size)
    for ii in range(mel.size):
        n=mel[ii]
        simpson_err[ii]=numpy.abs(integrate_cos_simpson(n)-1)
        simple_err[ii]=numpy.abs(integrate_cos_simple(n)-1)
    plt.plot(mel,simple_err)
    plt.plot(mel,simpson_err)
    ax=plt.gca()

    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.show()
