'''
Created on 31 Mar 2018

@author: kishore
'''
import Tkinter  as tk


class companyui:
    def __init__(self):
        window = tk.Tk()
        window.geometry('%dx%d+%d+%d' % (400, 400, 200, 200))
        title = tk.Label(text="This is label")
        title.grid()
        button = tk.Button(text="This is button")
        button.grid(row=1,column=1)
        entry = tk.Text( master=window,height=10,width=20)
        entry.grid(row=1,column=5)
        window.mainloop()
        