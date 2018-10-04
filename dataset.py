# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 22:33:35 2018

@author: MD SAIF UDDIN
"""
def datas():
    import tkinter
    import csv

    root = tkinter.Tk()

# open file
    with open("Grade_Marks_EC401.csv", newline = "") as file:
        reader = csv.reader(file)

   # r and c tell us where to grid the labels
        r = 0
        for col in reader:
            c = 0
            for row in col:
                label = tkinter.Label(root, width = 22, height = 1, \
                               text = row, relief = tkinter.RIDGE)
                label.grid(row = r, column = c)
                c += 1
            r += 1

    root.mainloop()

datas()