def linegraph():
        import numpy as np
        import matplotlib.pyplot as plt
        #import matplotlib.animation as animation
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np
        x=[]
        l=[]
        dataset=pd.read_csv('Grade_Marks_EC401.csv')
        mark=dataset.iloc[2:,4:5]
        mark=mark.values
        for  i in list(mark):
                l.append(int(i))
        

        year = [0, 20, 40, 60, 80, 100]
        pop_p= [34,43,51,55,67,100]
        pop_i= [43,54,58,65,69,95]
        physic=[45,55,69,76,84,91]
        plt.plot(year, pop_p, color='g')
        plt.plot(year, pop_i, color='orange')
        plt.plot(year,physic,color='b')
        plt.xlabel('Subject')
        plt.ylabel('Marks botained')
        plt.title('All subject marks comparision')
        plt.show()
linegraph()
