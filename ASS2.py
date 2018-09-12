#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
#    Sep 02, 2018 02:05:45 AM

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

import ASS2_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = YEAR_CREDENTIAL (root)
    ASS2_support.init(root, top)
    root.mainloop()

w = None
def create_YEAR_CREDENTIAL(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = YEAR_CREDENTIAL (w)
    ASS2_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_YEAR_CREDENTIAL():
    global w
    w.destroy()
    w = None


class YEAR_CREDENTIAL:
    def semcall2018(self):
        import SEM_PAGE2018
        SEM_PAGE2018.vp_start_gui()

    def semcall2015(self):
        import SEM_PAGE2015
        SEM_PAGE2015.vp_start_gui()

    def semcall2016(self):
        import SEM_PAGE2016
        SEM_PAGE2016.vp_start_gui()

    def semcall2017(self):
        import SEM_PAGE2017
        SEM_PAGE2017.vp_start_gui()

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

        top.geometry("569x431+429+121")
        top.title("YEAR CREDENTIAL")
        top.configure(borderwidth="20")
        top.configure(relief="groove")
        top.configure(background="#d8d7c7")
        top.configure(takefocus="023")
        top.configure(width="10")



        self.BUTTON = Button(top)
        self.BUTTON.place(relx=0.37, rely=0.19, height=34, width=127)
        self.BUTTON.configure(activebackground="#d9d9d9")
        self.BUTTON.configure(activeforeground="#000000")
        self.BUTTON.configure(background="#d9d9d9")
        self.BUTTON.configure(disabledforeground="#a3a3a3")
        self.BUTTON.configure(foreground="#000000")
        self.BUTTON.configure(highlightbackground="#d9d9d9")
        self.BUTTON.configure(highlightcolor="black")
        self.BUTTON.configure(pady="0")
        self.BUTTON.configure(text='''2015''')
        self.BUTTON.configure(width=127)
        self.BUTTON.configure(command=self.semcall2015)
        
        self.Button2 = Button(top)
        self.Button2.place(relx=0.37, rely=0.32, height=34, width=127)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''2016''')
        self.Button2.configure(width=127)
        self.Button2.configure(command=self.semcall2016)
         
        self.Button3 = Button(top)
        self.Button3.place(relx=0.37, rely=0.46, height=34, width=127)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''2017''')
        self.Button3.configure(width=127)
        self.Button3.configure(command=self.semcall2017)
         
        self.Button4 = Button(top)
        self.Button4.place(relx=0.37, rely=0.6, height=34, width=127)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''2018''')
        self.Button4.configure(width=127)
        self.Button4.configure(command=self.semcall2018)
        
        self.tLa43 = ttk.Label(top)
        self.tLa43.place(relx=0.32, rely=0.07, height=19, width=180)
        self.tLa43.configure(background="#d9d9d9")
        self.tLa43.configure(foreground="#000000")
        self.tLa43.configure(font="TkDefaultFont")
        self.tLa43.configure(relief=FLAT)
        self.tLa43.configure(text='''STUDENT CREDENTIAL PER YEAR''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)








if __name__ == '__main__':
    vp_start_gui()



