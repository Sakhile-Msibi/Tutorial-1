import numpy as np
class Complex:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
    def copy(self):
        return Complex(self.r,self.i)
    def __sub__(self,val):
        ans=self.copy()
        if isinstance(val,Complex):
            ans.r=ans.r+val.r
            ans.i=ans.i-val.i
        else:
            ans.r=ans.r-val
        return ans

    def __mul__(self,val):
        ans=self.copy()
        if isinstance(val,Complex):
            ans.r=self.r*val.r-self.i*val.i
            ans.i=self.r*val.i+self.i*val.r
        else:
            ans.r=ans.r*val
            ans.i=ans.i*val
        return ans

    def __div__(self,val):
        if isinstance(val,Complex):
            ans.r=self.r/val.r-self.i/val.i
            ans.i=self.r/val.i+self.i/val.r
        else:
            ans.r=ans.r/val
            ans.i=ans.i/val
        return ans
    def __repr__(self):
        if (self.i<0):
            return repr(self.r)+' - '+repr(-1*self.i) +'i'
        else:
            return repr(self.r)+' + '+repr(self.i) +'i'
