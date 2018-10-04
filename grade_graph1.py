# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 01:05:35 2018

@author:MD SAIF UDDIN
"""

def histogram():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    x=[]
    dataset=pd.read_csv('Grade_Marks_EC401.csv')
    mark=dataset.iloc[2:,4:5]
    mark=mark.values

    mu, sigma = 100, 10
    l=[]
    for i in list(mark):
        l.append(int(i))
    x=l
    #print(len(l))
    #x =[73,82,46,82,50,23,42,43,46,79,36,30,53,80,70,68,71,69,40,88,59,59,48,59,80,83,47,30,24,64,51,47,66,66,76,56,21,66,51,68,74,44,52,67,74,82,37,48,54,54,75,39,48,80,72,91,51,48,40,35,51]
    hist, bins = np.histogram(x, bins=61)
    width = 0.7 
    center = (bins[:-1] + bins[1:]) /2
    plt.bar(center, hist, align='center', width=width)
    plt.show()
histogram()