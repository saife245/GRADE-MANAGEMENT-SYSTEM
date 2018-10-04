#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
#    Sep 02, 2018 10:19:13 PM

import sys
import backend

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

import signup_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = CREATE_LOGIN_ID (root)
    signup_support.init(root, top)
    root.mainloop()

w = None
def create_CREATE_LOGIN_ID(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = CREATE_LOGIN_ID (w)
    signup_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_CREATE_LOGIN_ID():
    global w
    w.destroy()
    w = None


class CREATE_LOGIN_ID:
    def againlogin(self):
        signup_support.destroy_window()
        import LOGIN
        LOGIN.vp_start_gui()
        
    def linked_to_database(self):
        backend.insert(self.Entry1.get(),self.Entry2.get(),self.Entry3.get(),self.Entry4.get())
        print("connected to database")
        return

    def entry_search():
        j=backend.search(self.Entry3.get())
        print(j)
        return j
        
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

        top.geometry("549x498+450+105")
        top.title("CREATE LOGIN ID")
        top.configure(borderwidth="20")
        top.configure(relief="groove")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(takefocus="023")
        top.configure(width="10")



        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.42, rely=0.08, height=19, width=48)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''SIGN UP''')

        self.Entry1 = Entry(top)
        #e1=self.Entry1
        self.Entry1.place(relx=0.36, rely=0.18,height=30, relwidth=0.3)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=164)
        #E1=StringVar()
        #self.Entry1.configure(textvariable=E1)

        self.Entry2 = Entry(top)
        #e2=self.Entry2
        self.Entry2.place(relx=0.36, rely=0.32,height=30, relwidth=0.3)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=164)
        #E2=StringVar()
        #self.Entry2.configure(textvariable=E2)

        self.Entry3 = Entry(top)
        #e3=self.Entry3
        self.Entry3.place(relx=0.36, rely=0.6,height=30, relwidth=0.3)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(width=164)
        #E3=StringVar()
        #self.Entry3.configure(textvariable=E3)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.13, rely=0.2, height=21, width=40)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''NAME''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.07, rely=0.34, height=21, width=124)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''USER NAME/LOGIN ID''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.13, rely=0.62, height=21, width=68)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''PASSWORD''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.13, rely=0.48, height=21, width=54)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''EMAIL ID''')

        self.Entry4 = Entry(top)
        #e4=self.Entry4
        self.Entry4.place(relx=0.36, rely=0.46,height=30, relwidth=0.3)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(width=164)
        #E4=StringVar()
        #self.Entry4.configure(textvariable=E4)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.22, rely=0.76, height=34, width=97)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''CREATE''')
        self.Button1.configure(command=self.linked_to_database)
        self.Button1.configure(width=97)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.56, rely=0.76, height=34, width=97)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''BACK TO LOGIN''')
        self.Button2.configure(width=97)
        self.Button2.configure(command=self.againlogin)
        
        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

            
        






if __name__ == '__main__':
    vp_start_gui()



