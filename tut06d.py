import numpy
from matplotlib import pyplot as plt
#Question2-4
class Particles:
    def __init__(self,npart=300,fmax=1.0,u=1.0):
        self.f=numpy.arange(npart)/(0.0+npart)*fmax
        self.u=u*(fmax-self.f)/fmax

    def update(self,dt=0.01):
        self.f+=self.u*dt

    def get_density(self,dx=0.01):
        fmin=numpy.min(self.f)
        fmax=numpy.max(self.f)
        nbin=numpy.round(1+(fmax-fmin)/dx)
        ind=numpy.round( (self.f-fmin)/dx)
        rho=numpy.zeros(nbin)

        assert(ind.max()<nbin) 
        for i in numpy.arange(0,ind.size):
            rho[ind[i]]+=1.0
        fvector=numpy.arange(0,nbin)*dx+fmin
        return rho,fvector
if __name__=='__main__':
    part=Particles(npart=80000)
    plt.ion()
    plt.plot(part.f)
    plt.show()

    plt.clf()
    for ii in range(0,250):
        part.update(dt=0.01)
        rho,f=part.get_density()
        plt.plot(f,rho)
        plt.draw()
