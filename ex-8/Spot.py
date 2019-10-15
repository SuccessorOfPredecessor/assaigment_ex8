from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Spot():
    def __init__(self, spotname):
        try:
            self.im = Image.open(spotname).convert("L")
        except:
            self.im = spotname
        self.arr = np.array(self.im)
        self.width = self.im.size[0]
        self.depth = self.im.size[1]
        self.size = self.width*self.depth
        self.arrR = self.arr.reshape(1,self.size)[0]
        self.sumI = 0
        self.Ibar = 0
        self.row = 0
        self.column = 0
        self.D_row = 0
        self.D_row_R = 0
        self.D_column = 0
        self.D_column_R = 0
        self.sigma = 0
        self.getpoint()
        self.Dsigma()
        self.getsigma()

    def getpoint(self):
        self.sumI = np.sum(self.arr)
        self.Ibar = self.sumI/self.size
        row = 0
        column = 0
        for i in range(self.depth):
            for j in range(self.width):
                row += self.arr[i][j]*i
                column += self.arr[i][j]*j
        self.row = row/self.sumI
        self.column = column/self.sumI
        self.point = (self.row, self.column)

    def Dsigma(self):
        Dx = 0
        Dy = 0
        for i in range(self.depth):
            for j in range(self.width):
                Dx += self.arr[i][j]* (i - self.row)**2
                Dy += self.arr[i][j]* (j - self.column)**2
        self.D_row = math.sqrt(Dx/self.sumI)
        self.D_column = math.sqrt(Dy/self.sumI)
        
        self.D_row_R = self.D_row/self.depth
        self.D_column_R = self.D_column/self.width

    def imcut(self, box=None):
        if box == None:
            rmin = int(self.row-self.D_row if self.row-self.D_row>0 else 0)
            rmax = int(self.row+self.D_row if self.row-self.D_row>self.depth else self.depth)
            cmin = int(self.column-self.D_column if self.column-self.D_column>0 else 0)
            cmax = int(self.column+self.D_column if self.column+self.D_column>self.width else self.width)
            box = (cmin,rmin,cmax,rmax)
        return(self.im.crop(box))
    
    def bar3d(self, name):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        _x = np.arange(self.width)
        _y = np.arange(self.depth)
        _xx, _yy = np.meshgrid(_x, _y)
        x, y = _xx.ravel(), _yy.ravel()
        z = np.zeros_like(self.size)
        dx = np.ones_like(self.size)
        dy = np.ones_like(self.size)
        dz = self.arrR
        ax.bar3d(x,y,z,dx,dy,dz, shade=True)
        plt.savefig(name)
        plt.show()
    
    def getsigma(self):
        x = 0
        for i in range(1):
            x += math.pow((self.arrR[i]-self.Ibar),2)/self.Ibar
        self.sigma = math.sqrt(x/self.size)



box = (75, 75, 165, 135)