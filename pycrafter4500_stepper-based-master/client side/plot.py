import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pylab import *
from tkinter import *

class MyPlot(object):
    mpl.rcParams['toolbar'] = 'None'
    def __init__(self):
        #plt.ion()
        self.fig, self.ax = plt.subplots(facecolor=(0,0,0),figsize=(2,2),frameon=True)
        # self.fig, self.ax = plt.subplots()
        self.fig.dpi = 300
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
        self.ax.set_aspect('equal')
        plt.axis('off')
        self.fig.tight_layout()
        #plt.show()
        plt.pause(0.01)
        #mngr = plt.get_current_fig_manager()
        # to put it into the upper left corner for example:
        #mngr.window.setGeometry(50,100,640, 545)
        #geom = mngr.window.geometry()
        #print(geom)
        #x,y,dx,dy = geom.getRect()

    def clear(self):
        self.ax.lines = []          # delete all lines
        self.addRect(0,0,1,1,'black') # delete all patches (polygons)

    def addLine(self,x1,x2,y1,y2,lw=1):
        self.ax.plot([x1,x2],[y1,y2],'w-',linewidth=lw)

    def addRect(self,x,y,w,h,color='white'):
        self.ax.add_patch(patches.Rectangle((x, y),width=w,height=h,color=color,lw=0))

    def addCir(self,x,y,r,color='white'):
        self.ax.add_patch(patches.Circle((x,y),radius=r, color=color,lw=0))

    def addRing(self,x,y,r,w,start=0,end=360,color='white'):
        self.ax.add_patch(patches.Wedge((x, y), r, start, end, width=w, color=color,lw=0))

    def addPolygon(self,polygon):
        self.ax.add_patch(polygon)

    def addEllipse(self,x,y,w,h,color='white'):
        self.ax.add_patch(patches.Ellipse((x, y),width=w,height=h,color=color,lw=0))

    def show(self):
        plt.pause(0.005)
