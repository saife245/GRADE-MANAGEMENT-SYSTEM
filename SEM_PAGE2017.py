#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
#    Sep 02, 2018 03:05:54 PM

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

import SEM_PAGE_support2017

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = SEMESTER (root)
    SEM_PAGE_support2017.init(root, top)
    root.mainloop()

w = None
def create_SEMESTER(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = SEMESTER (w)
    SEM_PAGE_support2017.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_SEMESTER():
    global w
    w.destroy()
    w = None


class SEMESTER:
    def oddsem2017(self):
        import ODD_SEM2017
        ODD_SEM2017.vp_start_gui()

    def evensem2017(self):
        import EVEN_SEM2017
        EVEN_SEM2017.vp_start_gui()
        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+420+121")
        top.title("SEMESTER")
        top.configure(borderwidth="20")
        top.configure(relief="groove")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(takefocus="023")
        top.configure(width="10")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.1, rely=0.1, relheight=0.75, relwidth=0.8)

        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''SEMESTERS''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(width=490) 

        self.Button1 = Button(top)
        self.Button1.place(relx=0.35, rely=0.27, height=64, width=157)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''ODD SEM''')
        self.Button1.configure(width=157)
        self.Button1.configure(command=self.oddsem2017)
        
        self.Button2 = Button(top)
        self.Button2.place(relx=0.35, rely=0.51, height=64, width=157)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''EVEN SEM''')
        self.Button2.configure(width=157)
        self.Button2.configure(command=self.evensem2017)
        
        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)








if __name__ == '__main__':
    vp_start_gui()



