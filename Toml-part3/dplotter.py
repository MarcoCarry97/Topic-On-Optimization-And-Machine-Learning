# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:02:51 2022

@author: Marco-PC
"""

from matplotlib import pyplot as plt
import numpy as np
import os
import shutil as sh
import pandas as pd
import seaborn as sb
from seaborn_qqplot import pplot

#useful plots:
    #lineplot
    #pairplot
    #boxplot
    #scatterplot
    
def getCorrelationMatrix(data):
    return data.corr()

class Plotter:
    def __init__(self):
        self.xlabel="x"
        self.ylabel="y"
        self.ptitle="plot"
        self.size=20
        sb.set_style("whitegrid")
    
    def labels(self,x,y):
        self.xlabel=x
        self.ylabel=y
    
    def title(self,t):
        self.ptitle=t
    
    def show(self,data,delete=False,save=False,hue=None,dkind=None,vmin=-1,vmax=1):
        fig=plt.figure(figsize=(10,9))
        plt.xlabel(self.xlabel,fontsize=self.size)
        plt.ylabel(self.ylabel,fontsize=self.size)
        plt.title(self.ptitle,fontsize=self.size)
        
        #plot here
        
        if(os.path.exists("./plot") and delete and save):
            sh.rmtree("./plot")
        if(delete and save):
            os.mkdir("./plot")
        plt.show()
        fig.savefig(self.ptitle+".jpg")
        
    
class LinePlotter(Plotter):
    def __init__(self):
        super().__init__()
    
    def show(self,data,delete=False,save=False,hue=None,dkind=None,vmin=-1,vmax=1):
        fig=plt.figure(figsize=(10,9))
        plt.xlabel(self.xlabel,fontsize=self.size)
        plt.ylabel(self.ylabel,fontsize=self.size)
        plt.title(self.ptitle,fontsize=self.size)
        
        sb.lineplot(data=data,x=self.xlabel,y=self.ylabel)
        
        if(os.path.exists("./plot") and delete and save):
            sh.rmtree("./plot")
        if(delete and save):
            os.mkdir("./plot")
        plt.show()
        fig.savefig(self.ptitle+".jpg")
        
class PairPlotter(Plotter):
    def __init__(self):
        super().__init__()
    
    def show(self,data,delete=False,save=False,hue=None,dkind=None,vmin=-1,vmax=1):
        fig=plt.figure(figsize=(10,9))
        plt.xlabel(self.xlabel,fontsize=self.size)
        plt.ylabel(self.ylabel,fontsize=self.size)
        plt.title(self.ptitle,fontsize=self.size)
        
        sb.pairplot(data=data)
        
        if(os.path.exists("./plot") and delete and save):
            sh.rmtree("./plot")
        if(delete and save):
            os.mkdir("./plot")
        plt.show()
        fig.savefig(self.ptitle+".jpg")
        
class BoxPlotter(Plotter):
    def __init__(self):
        super().__init__()
    
    def show(self,data,delete=False,save=False,hue=None,dkind=None,vmin=-1,vmax=1):
        fig=plt.figure(figsize=(10,9))
        plt.xlabel(self.xlabel,fontsize=self.size)
        plt.ylabel(self.ylabel,fontsize=self.size)
        plt.title(self.ptitle,fontsize=self.size)
        
        sb.boxplot(x=self.xlabel,y=self.ylabel,data=data)
        
        if(os.path.exists("./plot") and delete and save):
            sh.rmtree("./plot")
        if(delete and save):
            os.mkdir("./plot")
        #plt.show()
        fig.savefig(self.ptitle+".jpg")
        
class ScatterPlotter(Plotter):
    def __init__(self):
        super().__init__()
    
    def show(self,data,delete=False,save=False,hue=None,dkind=None,vmin=-1,vmax=1):
        fig=plt.figure(figsize=(10,9))
        plt.xlabel(self.xlabel,fontsize=self.size)
        plt.ylabel(self.ylabel,fontsize=self.size)
        plt.title(self.ptitle,fontsize=self.size)
        
        sb.scatterplot(x=self.xlabel,y=self.ylabel,data=data)
        
        if(os.path.exists("./plot") and delete and save):
            sh.rmtree("./plot")
        if(delete and save):
            os.mkdir("./plot")
        #plt.show()
        fig.savefig(self.ptitle+".jpg")
        
class HeatMap(Plotter):
    def __init__(self):
        super().__init__()
        
    def show(self,data,delete=False,save=False,hue=None,dkind=None,vmin=-1,vmax=1):
        fig=plt.figure(figsize=(10,9))
        plt.xlabel(self.xlabel,fontsize=self.size)
        plt.ylabel(self.ylabel,fontsize=self.size)
        plt.title(self.ptitle,fontsize=self.size)
        
        corrMatrix=getCorrelationMatrix(data)
        sb.heatmap(corrMatrix,annot=True,cmap="Blues")
        
        if(os.path.exists("./plot") and delete and save):
            sh.rmtree("./plot")
        if(delete and save):
            os.mkdir("./plot")
        #plt.show()
        fig.savefig(self.ptitle+".jpg")
 
class QqPlotter(Plotter):
    def __init__(self):
        super().__init__()
        
    def show(self,data,delete=False,save=False,hue=None,dkind=None,vmin=-1,vmax=1):
        fig=plt.figure(figsize=(10,9))
        plt.xlabel(self.xlabel,fontsize=self.size)
        plt.ylabel(self.ylabel,fontsize=self.size)
        plt.title(self.ptitle,fontsize=self.size)
        
        pplot(data,x=self.xlabel,y=self.ylabel, kind="qq")
        
        if(os.path.exists("./plot") and delete and save):
            sh.rmtree("./plot")
        if(delete and save):
            os.mkdir("./plot")
        #plt.show()
        fig.savefig(self.ptitle+".jpg")
 
def boxplot(data,x,y,title,delete,save):
    p=BoxPlotter()
    p.labels(x, y)
    p.title(title)
    p.show(data,delete=delete,save=save)
    
def scatterplot(data,x,y,title,delete,save):
    p=ScatterPlotter()
    p.labels(x, y)
    p.title(title)
    p.show(data,delete=delete,save=save)
    
def pairplot(data,x,y,title,delete,save):
    p=PairPlotter()
    p.labels(x, y)
    p.title(title)
    p.show(data,delete=delete,save=save)
    
def lineplot(data,x,y,title,delete,save):
    p=LinePlotter()
    p.labels(x, y)
    p.title(title)
    p.show(data,delete=delete,save=save)
    
def heatmap(data,title,delete,save):
    p=HeatMap()
    p.title(title)
    p.show(data,delete=delete,save=save)
    
def qqplot(data,x,y,title,delete,save):
    p=QqPlotter()
    p.labels(x, y)
    p.title(title)
    p.show(data,delete=delete,save=save)