# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 18:34:51 2018

@author: praveen kumar
"""
def piechart():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    x=[]
    dataset=pd.read_csv('Grade_Marks_EC401.csv')
    mark=dataset.iloc[2:,4:5]
    mark=mark.values
    '''for i in mark:
    print(x) 
    print(np.array(mark))'''

    num_bins = 7
    #n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
    #plt.show()



    def cal(x1):
        count1=0
        count2=0
        count3=0
        count4=0
        count5=0
        count6=0
        count7=0
        l=[]
        for i in x1:
            if i>='82' and i<='100':
                count1 +=1
            elif i>='71' and i<='81':
                count2 +=1
            elif i>='58' and i<='70':
                count3 +=1
            elif i>='46' and i<='57':
                count4 +=1
            elif i>='39' and i<='45':
                count5 +=1
            elif i>='30' and i<='38':
                count6 +=1
            elif i<'30':
                count7+=1
        l.append(6)
        l.append(count2)
        l.append(count3)
        l.append(count4)
        l.append(count5)
        l.append(count6)
        l.append(count7)
        return l

    #Pie chart
    import matplotlib.pyplot as plotter

 

    # The slice names of a population distribution pie chart

    pieLabels = 'Excellent', 'Grade A', 'Grade B', 'Grade C', 'Grade D', 'Grade P','Grade F'

 

    # Population data

    #populationShare     = [59.69, 16, 9.94, 7.79, 5.68, 0.54]
    
    llist=list(mark)

    p=cal(llist)
    print(p)
    #print(sum(p))

    figureObject, axesObject = plotter.subplots()

 

    # Draw the pie chart

    axesObject.pie(p,

            labels=pieLabels,

            autopct='%1.2f',

            startangle=360)

 

    # Aspect ratio - equal means pie is a circle

    axesObject.axis('equal')
    plotter.show()
piechart()
'''
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
'''
