#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
#    Sep 04, 2018 12:54:49 AM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import ODD_SEM_support2018

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = SELECT_SEMESTER (root)
    ODD_SEM_support2018.init(root, top)
    root.mainloop()

w = None
def create_SELECT_SEMESTER(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = SELECT_SEMESTER (w)
    ODD_SEM_support2018.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_SELECT_SEMESTER():
    global w
    w.destroy()
    w = None


class SELECT_SEMESTER:
    def next1(self):
        ODD_SEM_support2018.destroy_window()
        import ANALYSE_RESULTS
        ANALYSE_RESULTS.vp_start_gui()
        
    def back(self):
        ODD_SEM_support2018.destroy_window()
        import SEM_PAGE2018
        SEM_PAGE2018.vp_start_gui()
        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("565x423+447+133")
        top.title("SELECT SEMESTER")
        top.configure(borderwidth="20")
        top.configure(relief="groove")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#000000")
        top.configure(takefocus="023")
        top.configure(width="10")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.44, rely=0.12, height=21, width=61)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''SEMESTER''')

        self.Button1 = Button(top)
        self.Button1.place(relx=0.25, rely=0.26, height=44, width=77)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''1ST SEM''')
        self.Button1.configure(width=77)
        self.Button1.configure(command = self.next1)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.62, rely=0.26, height=44, width=77)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''3RD SEM''')
        self.Button2.configure(width=77)
        self.Button2.configure(command = self.next1)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.25, rely=0.52, height=44, width=77)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''5TH SEM''')
        self.Button3.configure(width=77)
        self.Button3.configure(command = self.next1)

        self.Button4 = Button(top)
        self.Button4.place(relx=0.62, rely=0.52, height=44, width=77)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''7TH SEM''')
        self.Button4.configure(width=77)
        self.Button4.configure(command = self.next1)

        self.Button5 = Button(top)
        self.Button5.place(relx=0.34, rely=0.73, height=44, width=187)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''BACK''')
        self.Button5.configure(width=187)
        self.Button5.configure(command=self.back)





if __name__ == '__main__':
    vp_start_gui()



