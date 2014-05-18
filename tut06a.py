import numpy as np
from matplotlib import pyplot as plt
class advect:
    def __init__(self):
        x=np.zeros(300)
        x[300/3:2*300/3]=1.0;
        self.x=x
        self.v=1.0
        self.dx=1.0
    def get_bc_periodic(self):
        self.x[0]=self.x[-2]
        self.x[-1]=self.x[1]
    def update(self):
        self.get_bc_periodic()
        delt=self.x[1:]-self.x[0:-1]
        self.x[1:-1]+=self.v*1.0/self.dx*delt[1:]

if __name__=='__main__':
    stuff=advect()
    plt.ion()
    plt.plot(stuff.x)
    plt.show()
    for i in range(0,300):
        stuff.update()
        plt.clf()
        plt.plot(stuff.x)
        plt.draw()
