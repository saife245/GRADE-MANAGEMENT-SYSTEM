#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#    Sep 26, 2018 01:16:48 PM

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

import ANALYSE_RESULTS_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = ANALYSE_RESULTS (root)
    ANALYSE_RESULTS_support.init(root, top)
    root.mainloop()

w = None
def create_ANALYSE_RESULTS(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = ANALYSE_RESULTS (w)
    ANALYSE_RESULTS_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_ANALYSE_RESULTS():
    global w
    w.destroy()
    w = None

class ANALYSE_RESULTS:
    def line(self):
        import line_graph
        line_graph.linegraph()
        
    def dataa(self):
        import dataset
        dataset.datas()
        
    def pie(self):
        import grade_graph
        grade_graph.piechart()
    
    def histo(self):
        import grade_graph1
        grade_graph1.histogram()
        
    def back(self):
        ANALYSE_RESULTS_support.destroy_window()
        import ODD_SEM2018
        ODD_SEM2018.vp_start_gui()
        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font14 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("600x420+449+144")
        top.title("ANALYSE RESULTS")
        top.configure(borderwidth="20")
        top.configure(relief="groove")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.configure(takefocus="023")
        top.configure(width="8")



        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.1, rely=0.11, relheight=0.74
                , relwidth=0.78)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''RESULT ANALYSIS''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(width=470)

        self.Button1 = Button(self.Labelframe1)
        self.Button1.place(relx=0.64, rely=0.15, height=34, width=67, y=-12)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SHOW''')
        self.Button1.configure(width=67)
        self.Button1.configure(command = self.dataa)

        self.Button2 = Button(self.Labelframe1)
        self.Button2.place(relx=0.64, rely=0.34, height=34, width=67, y=-12)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font9)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''SHOW''')
        self.Button2.configure(width=67)
        self.Button2.configure(command = self.histo)

        self.Button3 = Button(self.Labelframe1)
        self.Button3.place(relx=0.64, rely=0.54, height=34, width=67, y=-12)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font9)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''SHOW''')
        self.Button3.configure(width=67)
        self.Button3.configure(command = self.pie)

        self.Button5 = Button(self.Labelframe1)
        self.Button5.place(relx=0.64, rely=0.75, height=34, width=67, y=-12)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font9)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''SHOW''')
        self.Button5.configure(width=67)
        self.Button5.configure(command = self.line)

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.17, rely=0.15, height=41, width=104, y=-12)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font14)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''MARKS''')
        self.Label1.configure(width=104)

        self.Label2 = Label(self.Labelframe1)
        self.Label2.place(relx=0.21, rely=0.36, height=21, width=72, y=-12)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font14)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''HISTOGRAM''')

        self.Label3 = Label(self.Labelframe1)
        self.Label3.place(relx=0.19, rely=0.54, height=31, width=94, y=-12)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font14)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''PIE CHART''')
        self.Label3.configure(width=94)

        self.Label4 = Label(self.Labelframe1)
        self.Label4.place(relx=0.19, rely=0.75, height=31, width=94, y=-12)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font14)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''LINE GRAPH''')
        self.Label4.configure(width=94)

        self.Button4 = Button(top)
        self.Button4.place(relx=0.05, rely=0.89, height=24, width=50)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''BACK''')
        self.Button4.configure(width=47)
        self.Button4.configure(command = self.back)

if __name__ == '__main__':
    vp_start_gui()
