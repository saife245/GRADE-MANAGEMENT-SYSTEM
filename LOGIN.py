#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
#    Sep 02, 2018 11:53:11 AM

import sys
from tkinter import messagebox
import signup

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

import LOGIN_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Login_page (root)
    LOGIN_support.init(root, top)
    root.mainloop()

w = None
def create_Login_page(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Login_page (w)
    LOGIN_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Login_page():
    global w
    w.destroy()
    w = None


class Login_page:
    def sign_up(self):
        import signup
        signup.vp_start_gui()

    def cancellogin(self):
        msg = messagebox.askyesno("Login page", "Are you sure , you want to cancel login?")
        if (msg):
          exit()

    def loginuser(self):
        name=self.txtUsers.get()
        passwd=self.txtPassword.get()

        if name == "saifuddin" and passwd == "fuck":
            messagebox.showinfo("Login Page", "The login is succesfull")
            import ASS2
            ASS2.vp_start_gui()
            
        else:
            messagebox.showwarning("Login Page", "login id and password is incorrect")


            
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

        top.geometry("600x450+408+139")
        top.title("Login page")
        top.configure(borderwidth="20")
        top.configure(relief="ridge")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.configure(takefocus="23")
        top.configure(width="10")


        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.1, rely=0.11, relheight=0.81, relwidth=0.8)

        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''GRADE MANAGEMENT SYSTEM''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(width=490)
        
        self.Label1 = Label(top)
        self.Label1.place(relx=0.22, rely=0.24, height=21, width=55)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''LOGIN ID''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.22, rely=0.44, height=21, width=68)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''PASSWORD''')

               
        self.txtUsers = Entry(top)
        self.txtUsers.place(relx=0.38, rely=0.24,height=30, relwidth=0.29)
        self.txtUsers.configure(background="white")
        self.txtUsers.configure(disabledforeground="#a3a3a3")
        self.txtUsers.configure(font="TkFixedFont")
        self.txtUsers.configure(foreground="#000000")
        self.txtUsers.configure(highlightbackground="#d9d9d9")
        self.txtUsers.configure(highlightcolor="black")
        self.txtUsers.configure(insertbackground="black")
        self.txtUsers.configure(selectbackground="#c4c4c4")
        self.txtUsers.configure(selectforeground="black")

        self.txtPassword = Entry(top, show='*')
        self.txtPassword.place(relx=0.38, rely=0.42,height=30, relwidth=0.29)
        self.txtPassword.configure(background="white")
        self.txtPassword.configure(disabledforeground="#a3a3a3")
        self.txtPassword.configure(font="TkFixedFont")
        self.txtPassword.configure(foreground="#000000")
        self.txtPassword.configure(highlightbackground="#d9d9d9")
        self.txtPassword.configure(highlightcolor="black")
        self.txtPassword.configure(insertbackground="black")
        self.txtPassword.configure(selectbackground="#c4c4c4")
        self.txtPassword.configure(selectforeground="black")

        self.Button1 = Button(top)
        self.Button1.place(relx=0.37, rely=0.6, height=24, width=46)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''LOGIN''')
        self.Button1.configure(command=self.loginuser)
        
        self.Button2 = Button(top)
        self.Button2.place(relx=0.6, rely=0.6, height=24, width=56)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''CANCEL''')
        self.Button2.configure(command=self.cancellogin)
        
        self.Button3 = Button(top)
        self.Button3.place(relx=0.37, rely=0.73, height=44, width=187)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''SIGN UP''')
        self.Button3.configure(width=187)
        self.Button3.configure(command=self.sign_up)




if __name__ == '__main__':
    vp_start_gui()



